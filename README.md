# Battery Stack

A multi-package repository for battery management and analytics, built with Python and future Rust components.

## Project Structure

```
battery-stack/
├── pkgs/                    # Python packages
│   ├── battery-data/        # Data handling and schemas
│   ├── battery-models/      # Battery modeling and algorithms
│   ├── battery-runtime/     # Runtime and scheduling
│   ├── batteryd/           # Battery daemon
│   └── monitor-ui/         # Monitoring UI components
├── apps/                   # Applications
│   └── observer-demo/      # Demo application
├── .devcontainer/          # VS Code dev container config
├── Dockerfile              # Multi-stage Docker build
├── docker-compose.yml      # Docker Compose services
└── pyproject.toml         # Root project configuration
```

## Development Setup

### Option 1: Local Development with Hatch

1. Install hatch:
   ```bash
   pip install hatch
   ```

2. Run tests:
   ```bash
   hatch run test
   ```

3. Run linting:
   ```bash
   hatch run lint
   ```

4. Format code:
   ```bash
   hatch run format
   ```

### Option 2: Docker Development

#### Using Docker Compose (Recommended)

1. **Development environment** (interactive shell with mounted volumes):
   ```bash
   docker-compose up dev
   ```
   This starts a container with your code mounted, allowing live editing.

2. **Run tests**:
   ```bash
   docker-compose run test
   ```

3. **Production build**:
   ```bash
   docker-compose up prod
   ```

#### Using Docker directly

1. **Build development image**:
   ```bash
   docker build --target development -t battery-stack:dev .
   ```

2. **Run development container**:
   ```bash
   docker run -it -v $(pwd):/workspace -p 8000:8000 battery-stack:dev
   ```

3. **Build and run tests**:
   ```bash
   docker build --target testing -t battery-stack:test .
   docker run battery-stack:test
   ```

### Option 3: VS Code Dev Container

1. Open the project in VS Code
2. Install the "Dev Containers" extension
3. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
4. Select "Dev Containers: Reopen in Container"

The dev container includes:
- Python 3.11
- Node.js 22 (for future frontend components)
- Rust (for future Rust packages)
- All necessary VS Code extensions
- Automatic hatch environment setup

## Package Development

Each package in `pkgs/` is independently installable:

```bash
# Install a specific package in development mode
pip install -e pkgs/battery-data[dev]

# Install all packages
pip install -e pkgs/battery-data[dev] -e pkgs/battery-models[dev] -e pkgs/battery-runtime[dev] -e pkgs/batteryd[dev]
```

## Testing

The project uses pytest for testing. Tests are organized per package:

```bash
# Run all tests
hatch run test

# Run tests for a specific package
pytest pkgs/battery-data/tests/

# Run with coverage
hatch run test:cov
```

## Docker Services

The `docker-compose.yml` defines three services:

- **dev**: Development environment with live code mounting
- **test**: Testing environment that runs the test suite
- **prod**: Production-ready minimal image

## Environment Variables

Common environment variables:

- `PYTHONPATH`: Set to workspace/app path
- `PYTHONUNBUFFERED`: Ensures Python output is not buffered
- `PYTHONDONTWRITEBYTECODE`: Prevents Python from writing .pyc files

## Ports

The following ports are exposed:

- `8000`: Main application
- `8080`: Development server
- `3000`: Frontend development server

## Contributing

1. Make changes to the relevant package in `pkgs/` or `apps/`
2. Run tests: `hatch run test`
3. Run linting: `hatch run lint`
4. Format code: `hatch run format`
5. Commit your changes

## Future Plans

- Add Rust packages for performance-critical components
- Implement CI/CD pipeline using the Docker testing stage
- Add monitoring and observability features
- Expand the UI components
