ARG PYTHON_VERSION=3.10

FROM python:3.11-slim-bookworm@sha256:f06d01d4ba3f8ad5af45a3ec87df19c1d317d8e8961edc0fabda61811af6f7cf AS python3.11
FROM python:3.14-slim-bookworm@sha256:f8417a152ae83c696bee8861ed715acd93a9c9a925cd868325bc0afd788537e6 AS python3.14
FROM python:3.10-slim-bookworm@sha256:5be5aaecb962a41567bc8041f1e9e3432cb085b037fe057f9a562630b2e4b370 AS python3.10
FROM python:3.12-slim-bookworm@sha256:6a0e06f5ba0b373d051aabd3fffb9b873f27f9a2a3a14bcbe37dee6f0e3bbc70 AS python3.12
FROM python:3.13-slim-bookworm@sha256:a881a81282cca8c57f97014867fa651def1b3799030cc6b1cff45ed55ba8ef36 AS python3.13
FROM python:3.15-slim-bookworm@sha256:575f8bc12ec26542e0678bc6b60e385218248019d433157ec327264a78c3a853 AS python3.15
FROM ghcr.io/astral-sh/uv:0.13.5@sha256:32a7bb39b496babbd997b0a39a4d66c126bdaf5661b302bf6f06abda8deca6ff AS uv

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
