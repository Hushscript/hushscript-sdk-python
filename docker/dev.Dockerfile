ARG PYTHON_VERSION=3.10

FROM python:3.11-slim-trixie@sha256:673719e071ecf27434fd2635bbd8d00f49f4fdd81f243143438a42ced8bedf60 AS python3.11
FROM python:3.14-slim-trixie@sha256:cd89c30eda26ee911a4611b18680086e0ea42e6f5f8cbe653d07fa7958c9cec8 AS python3.14
FROM python:3.10-slim-trixie@sha256:6ff506466f8b1e981719b468cc0023b8ef000b983cdec0eafe119d01f379e31d AS python3.10
FROM python:3.12-slim-trixie@sha256:aa943ce411423c7582288f18707ff66eddcbaeb510502d747a72aeb34f30d159 AS python3.12
FROM python:3.13-slim-trixie@sha256:2d44738ebf4ce5f63b9d9ea871e9c7cfdc0426f7b0c97cac915fd88ded1d86bb AS python3.13
FROM python:3.15-slim-trixie@sha256:94d3426f1def7db4a106a232ac121bfd975393e5dfd40a619b955fae45fe7913 AS python3.15
FROM ghcr.io/astral-sh/uv:0.13.6@sha256:af22a52f5eafef3d78e551599d405c02df61919d18028f0cea8eda93bc9986d0 AS uv

# The runtime stages above are digest-pinned images; the build arg only selects one.
# hadolint ignore=DL3006
FROM python${PYTHON_VERSION} AS base
RUN groupadd --gid 10001 dev && useradd --uid 10001 --gid 10001 --no-create-home --shell /usr/sbin/nologin dev
COPY --from=uv /uv /usr/local/bin/uv
ENV HOME=/tmp \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    UV_CACHE_DIR=/tmp/uv-cache \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON_PREFERENCE=only-system \
    UV_NO_PROGRESS=1
WORKDIR /work

FROM base AS deps
COPY pyproject.toml uv.lock ./
RUN UV_PROJECT_ENVIRONMENT=/work/.venv uv sync --frozen --no-install-project

# The tools live in /work/.venv/bin; src is on PYTHONPATH instead of being installed, so the
# read-only container never has to write into the environment.
FROM base AS dev
ENV PATH=/work/.venv/bin:$PATH \
    PYTHONPATH=/work/src \
    RUFF_CACHE_DIR=/tmp/ruff-cache \
    COVERAGE_FILE=/tmp/.coverage \
    HYPOTHESIS_STORAGE_DIRECTORY=/tmp/hypothesis
COPY --from=deps /work/.venv .venv
COPY --chown=10001:10001 . .
USER 10001:10001

# Runtime dependencies only: `just build` installs the built wheel next to these with no network.
FROM base AS proddeps
COPY pyproject.toml uv.lock ./
RUN UV_PROJECT_ENVIRONMENT=/opt/venv uv sync --frozen --no-install-project --no-dev
