# Use the official Python lightweight image
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

# Install uv
# COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

uv pip install keyrings.google-artifactregistry-auth
EXPORT UV_KEYRING_PROVIDER=subprocess

# Install the project into /app
COPY . /app
WORKDIR /app

# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN uv sync

EXPOSE $PORT

# Run the FastMCP server
CMD ["uv", "run", "server.py"]