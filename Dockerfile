# Multi-stage Dockerfile for battery-stack development and testing
FROM python:3.11-slim as base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Rust (for future Rust packages)
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Set working directory
WORKDIR /workspace

# Copy project files
COPY pyproject.toml ./
COPY pkgs/ ./pkgs/
COPY apps/ ./apps/

# Install hatch
RUN pip install hatch

# Development stage
FROM base as development

# Install all packages in development mode
RUN hatch env create

# Expose common ports for development
EXPOSE 8000 8080 3000

# Default command for development
CMD ["bash"]

# Testing stage
FROM base as testing

# Install test dependencies and run tests
RUN hatch run test

# Production stage (minimal)
FROM python:3.11-slim as production

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Copy only necessary files
COPY pyproject.toml ./
COPY pkgs/ ./pkgs/
COPY apps/ ./apps/

# Install only production dependencies
RUN pip install --no-cache-dir hatch && \
    hatch env create && \
    pip install --no-cache-dir -e pkgs/battery-data -e pkgs/battery-models -e pkgs/battery-runtime -e pkgs/batteryd

# Default production command
CMD ["python", "-m", "batteryd"]
