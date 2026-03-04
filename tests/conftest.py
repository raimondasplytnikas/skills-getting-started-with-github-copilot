import copy
import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture(autouse=True)
def reset_activities():
    """Ensure the global activities dict is restored after each test."""
    original = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original)


@pytest.fixture

def client():
    """Return a TestClient instance scoped to the application."""
    return TestClient(app)
