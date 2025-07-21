from collections.abc import Generator
from typing import Any

import pytest
from fastapi.testclient import TestClient

from src.service.api.main import app


@pytest.fixture(scope="function")
def client() -> Generator[TestClient, Any, Any]:
    """
    Provides a FastAPI TestClient instance for functional tests.

    The client is scoped per function to ensure isolation and avoid
    side effects between tests.

    Yields:
        TestClient: An instance of the FastAPI test client.
    """
    with TestClient(app=app, base_url="http://localhost:8000") as client:
        yield client
