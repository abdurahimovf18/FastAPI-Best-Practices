FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install uv globally 
RUN pip install uv

# Copy pyproject.toml 
COPY pyproject.toml .

# Copy uv.lock
COPY uv.lock .

# Sync dependencies based on pyproject.toml
RUN uv sync

# Now copy the full app code
COPY . .
