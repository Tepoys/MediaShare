# Based on multistage.Dockerfile from: 
# https://github.com/benitomartin/uv-docker-benchmark
#
# Copyright (c) 2024 Benito Martin
#
# The original work is licensed under the MIT license
# See ../THIRD-PARTY-NOTICES for the full license


# Using python 3.14 for this project
FROM ghcr.io/astral-sh/uv:0.12.7-python3.14-trixie-slim AS builder
# Have uv compile .py into bytecode .pyc, and have uv copy instead of linking files
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

# Dont need uv to download python as we are using a python docker image
ENV UV_PYTHON_DOWNLOADS=0

# set working directory
WORKDIR /app
# have uv install only the project dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev
# Copy everything  over from the base of backend onto the docker image
ADD . /app
# Install the project onto the docker iamge
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev


# Then, use a final image without uv
FROM python:3.14-slim-trixie

# Copy the application from the builder
COPY --from=builder --chown=app:app /app /app

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Run the FastAPI application by default
CMD ["fastapi", "dev", "--host", "0.0.0.0", "./app/app/main.py"]
