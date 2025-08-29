# CI Setup for Battery Stack

This document describes the GitHub Actions CI setup for the battery-stack monorepo.

## Overview

The CI pipeline includes comprehensive testing, linting, type checking, and Docker builds across multiple Python versions.

## CI Jobs

### 1. Lint (`lint`)
- Runs `ruff` linting on all packages and apps
- Checks code formatting with `ruff format --check`
- Ensures code follows project style guidelines

### 2. Type Check (`type-check`)
- Runs `mypy` type checking on all packages
- Currently set to `continue-on-error: true` to allow gradual type adoption
- Installs all packages before type checking

### 3. Unit Tests (`test`)
- Tests each package individually using a matrix strategy
- Packages tested: `battery-data`, `battery-models`, `battery-runtime`, `batteryd`
- Runs on Python 3.11
- Uses individual package installation for isolation

### 4. Test Coverage (`test-coverage`)
- Runs all tests with coverage reporting
- Installs all packages in the same environment
- Uploads coverage to Codecov (requires `CODECOV_TOKEN` secret)
- Coverage reporting set to not fail CI if upload fails

### 5. End-to-End Observer Demo (`e2e-observer`)
- Tests the complete observer demo application
- Ensures all packages work together correctly
- Validates the real-world usage scenario

### 6. Docker Build (`docker-build`)
- Builds the Docker image
- Tests that all packages can be imported in the container
- Validates containerized deployment

### 7. Multi-Python Testing (`multi-python`)
- Tests on Python 3.11 and 3.12
- Ensures compatibility across supported Python versions

## Local Development

### Running Tests
```bash
# Run all tests
hatch run test

# Run tests with coverage
hatch run test:cov

# Run individual package tests
pytest pkgs/battery-data/tests -v
```

### Linting and Formatting
```bash
# Check linting
hatch run lint

# Auto-format code
hatch run format

# Type checking
hatch run type-check
```

### Installing Packages
```bash
# Install all packages in development mode
hatch run install-packages
```

## Configuration

### Hatch Environments
- **default**: Main development environment with all tools
- **test**: Dedicated testing environment with coverage support

### Ruff Configuration
- Line length: 100 characters
- Target Python version: 3.11
- Ignores N806 (uppercase variable names) for mathematical notation

### MyPy Configuration
- Strict mode enabled
- Ignores missing imports for external packages
- Python 3.11 target

### Pytest Configuration
- Verbose output by default
- Test discovery in `pkgs/` directory
- Supports both `test_*.py` and `*_test.py` patterns

## Secrets Required

For full CI functionality, set up these GitHub repository secrets:
- `CODECOV_TOKEN`: For coverage reporting (optional)

## Troubleshooting

### Type Checking Failures
Type checking is currently set to continue on error. To fix type issues:
1. Run `hatch run type-check` locally
2. Add type annotations to functions missing them
3. Fix any type mismatches reported

### Coverage Issues
If coverage reporting fails:
1. Ensure all packages are properly installed
2. Check that test files are importing the correct modules
3. Verify coverage configuration in `pyproject.toml`

### Docker Build Issues
If Docker builds fail:
1. Check that all dependencies are properly specified in `pyproject.toml` files
2. Ensure the Dockerfile correctly installs all packages
3. Test locally with `docker build -t battery-stack:test .`
