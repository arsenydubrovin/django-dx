from app.test.api_client import AppTestClient
import pytest
from mixer.backend.django import mixer as _mixer


@pytest.fixture
def api():
    return AppTestClient()


@pytest.fixture
def mixer():
    return _mixer
