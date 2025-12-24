"""
Pytest configuration and shared fixtures for Cohen House Concierge tests
"""

import os
import sys
import pytest
from unittest.mock import Mock, AsyncMock, patch

# Add app directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Set test environment
os.environ["ENVIRONMENT"] = "test"
os.environ["OPENAI_API_KEY"] = "sk-test-mock-key"
os.environ["ELEVENLABS_API_KEY"] = "test-elevenlabs-mock-key"


@pytest.fixture(scope="session")
def test_app():
    """
    Create FastAPI app instance for testing.
    Using session scope to avoid recreating the app for each test.
    """
    from app.main import app
    return app


@pytest.fixture
def client(test_app):
    """
    Synchronous test client for FastAPI endpoints.
    Use this for testing non-async endpoints.
    """
    from fastapi.testclient import TestClient
    with TestClient(test_app) as test_client:
        yield test_client


@pytest.fixture
async def async_client(test_app):
    """
    Asynchronous test client for FastAPI endpoints.
    Use this for testing async endpoints and WebSocket connections.
    """
    from httpx import AsyncClient, ASGITransport
    async with AsyncClient(transport=ASGITransport(app=test_app), base_url="http://test") as ac:
        yield ac


@pytest.fixture
def mock_openai_response():
    """Mock OpenAI API response"""
    return {
        "text": "This is a test response from the AI assistant.",
        "action": None
    }


@pytest.fixture
def mock_whisper_response():
    """Mock Whisper transcription response"""
    return {
        "text": "This is a test transcription",
        "language": "en"
    }


@pytest.fixture
def mock_elevenlabs_response():
    """Mock ElevenLabs TTS response"""
    return "/tmp/tts_test_audio.mp3"


@pytest.fixture
def mock_openai_assistant(mock_openai_response):
    """Mock the OpenAI assistant"""
    with patch("app.main.assistant") as mock_assistant:
        mock_assistant.ask = AsyncMock(return_value=mock_openai_response)
        yield mock_assistant


@pytest.fixture
def mock_whisper(mock_whisper_response):
    """Mock Whisper speech recognition"""
    with patch("app.openai_speech.get_speech_client") as mock_client:
        mock_instance = Mock()
        mock_instance.transcribe_audio = AsyncMock(
            return_value=(mock_whisper_response["text"], mock_whisper_response["language"])
        )
        mock_client.return_value = mock_instance
        yield mock_client


@pytest.fixture
def mock_elevenlabs(mock_elevenlabs_response):
    """Mock ElevenLabs TTS"""
    with patch("app.main.text_to_speech") as mock_tts:
        mock_tts.return_value = AsyncMock(return_value=mock_elevenlabs_response)
        yield mock_tts


@pytest.fixture
def mock_spotify():
    """Mock Spotify control"""
    with patch("app.main.spotify") as mock_spotify:
        mock_spotify.is_music_playing.return_value = False
        mock_spotify.play_pizzica_di_san_vito = Mock()
        mock_spotify.play_fun_song = Mock()
        mock_spotify.open_spotify = Mock()
        yield mock_spotify


@pytest.fixture
def mock_ring():
    """Mock Ring doorbell"""
    with patch("app.ring_client.RingDoorbell") as mock_ring:
        mock_instance = Mock()
        mock_instance.initialize = AsyncMock(return_value=True)
        mock_ring.return_value = mock_instance
        yield mock_ring


@pytest.fixture
def sample_audio_file():
    """Create a sample audio file for testing"""
    import io
    audio_content = b"fake audio content for testing"
    return io.BytesIO(audio_content)


@pytest.fixture
def sample_face_image():
    """Create a sample base64 encoded image for face recognition testing"""
    import base64
    # 1x1 transparent PNG
    img_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82'
    return base64.b64encode(img_data).decode('utf-8')


@pytest.fixture(autouse=True)
def reset_mocks():
    """Reset all mocks between tests"""
    yield
    # Cleanup happens automatically with pytest


# Pytest markers
def pytest_configure(config):
    """Configure custom pytest markers"""
    config.addinivalue_line("markers", "unit: Unit tests")
    config.addinivalue_line("markers", "integration: Integration tests")
    config.addinivalue_line("markers", "e2e: End-to-end tests")
    config.addinivalue_line("markers", "async: Async tests")
    config.addinivalue_line("markers", "slow: Slow-running tests")
    config.addinivalue_line("markers", "external: Tests calling external APIs")
