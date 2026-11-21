ARG PYTHON_VERSION=3.10

FROM python:3.15-slim-trixie@sha256:65a65fc7b30b06cb6df4930fd4650697cb23f4c2698ab81fc87e4b031bc36928 AS python3.11
FROM python:3.15-slim-trixie@sha256:65a65fc7b30b06cb6df4930fd4650697cb23f4c2698ab81fc87e4b031bc36928 AS python3.14
FROM python:3.15-slim-trixie@sha256:65a65fc7b30b06cb6df4930fd4650697cb23f4c2698ab81fc87e4b031bc36928 AS python3.10
FROM python:3.15-slim-trixie@sha256:65a65fc7b30b06cb6df4930fd4650697cb23f4c2698ab81fc87e4b031bc36928 AS python3.12
FROM python:3.15-slim-trixie@sha256:65a65fc7b30b06cb6df4930fd4650697cb23f4c2698ab81fc87e4b031bc36928 AS python3.13
FROM python:3.15-slim-trixie@sha256:65a65fc7b30b06cb6df4930fd4650697cb23f4c2698ab81fc87e4b031bc36928 AS python3.15
FROM ghcr.io/astral-sh/uv:0.13.7@sha256:96f40d3904aad8d0bd010539001d36c8e2188b981e1334471a90c4a1d93bb490 AS uv

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
