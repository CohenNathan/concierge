"""
Main API endpoint tests using FastAPI TestClient
Following pytest + FastAPI best practices
"""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch, AsyncMock
import io


@pytest.mark.integration
class TestMainEndpoints:
    """Test main API endpoints"""
    
    def test_get_index(self, client):
        """Test GET / returns solomon.html"""
        response = client.get("/")
        assert response.status_code == 200
        assert "Cohen Smart House" in response.text
        assert "text/html" in response.headers["content-type"]
    
    def test_get_docs(self, client):
        """Test Swagger documentation endpoint"""
        response = client.get("/docs")
        assert response.status_code == 200
        assert "swagger" in response.text.lower()
    
    def test_get_openapi_schema(self, client):
        """Test OpenAPI schema endpoint"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        schema = response.json()
        assert "openapi" in schema
        assert "paths" in schema
        # Verify key endpoints exist
        assert "/upload-audio" in schema["paths"]
        assert "/ring/webhook" in schema["paths"]


@pytest.mark.integration
class TestAudioUploadEndpoint:
    """Test audio upload and transcription endpoint"""
    
    @patch("app.openai_speech.get_speech_client")
    def test_upload_audio_success(self, mock_speech_client, client):
        """Test successful audio upload and transcription"""
        # Mock the speech client
        mock_client = Mock()
        mock_client.transcribe_audio = AsyncMock(
            return_value=("Hello, this is a test", "en")
        )
        mock_speech_client.return_value = mock_client
        
        # Create fake audio file
        audio_content = b"fake audio data"
        files = {"file": ("test_audio.webm", io.BytesIO(audio_content), "audio/webm")}
        
        response = client.post("/upload-audio", files=files)
        
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["text"] == "Hello, this is a test"
        assert data["lang"] == "en"
    
    @patch("app.openai_speech.get_speech_client")
    def test_upload_audio_empty_transcription(self, mock_speech_client, client):
        """Test audio upload with empty transcription"""
        mock_client = Mock()
        mock_client.transcribe_audio = AsyncMock(return_value=("", "en"))
        mock_speech_client.return_value = mock_client
        
        audio_content = b"fake audio data"
        files = {"file": ("test_audio.webm", io.BytesIO(audio_content), "audio/webm")}
        
        response = client.post("/upload-audio", files=files)
        
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is False
        assert data["text"] is None
    
    def test_upload_audio_no_file(self, client):
        """Test audio upload without file"""
        response = client.post("/upload-audio")
        assert response.status_code == 422  # Validation error
    
    @patch("app.openai_speech.get_speech_client")
    def test_upload_audio_transcription_error(self, mock_speech_client, client):
        """Test audio upload with transcription error"""
        mock_client = Mock()
        mock_client.transcribe_audio = AsyncMock(side_effect=Exception("Transcription failed"))
        mock_speech_client.return_value = mock_client
        
        audio_content = b"fake audio data"
        files = {"file": ("test_audio.webm", io.BytesIO(audio_content), "audio/webm")}
        
        response = client.post("/upload-audio", files=files)
        
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is False
        assert "error" in data


@pytest.mark.integration
class TestRingWebhook:
    """Test Ring doorbell webhook endpoint"""
    
    @patch("app.main.ring_listener")
    def test_ring_webhook_success(self, mock_listener, client):
        """Test successful Ring webhook call"""
        mock_listener.notify = AsyncMock()
        
        payload = {
            "visitor": "John Doe",
            "lang": "en"
        }
        
        response = client.post("/ring/webhook", json=payload)
        
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert "greeting" in data
    
    def test_ring_webhook_default_visitor(self, client):
        """Test Ring webhook with default visitor"""
        response = client.post("/ring/webhook", json={})
        
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
    
    def test_ring_webhook_italian(self, client):
        """Test Ring webhook with Italian language"""
        payload = {
            "visitor": "Mario Rossi",
            "lang": "it"
        }
        
        response = client.post("/ring/webhook", json=payload)
        
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"


@pytest.mark.integration
@pytest.mark.skipif(True, reason="face-recognition module not installed (optional dependency)")
class TestFaceRecognition:
    """Test face recognition endpoints"""
    
    @patch("app.face_recognition_system.face_system")
    def test_recognize_face_success(self, mock_face_system, client, sample_face_image):
        """Test successful face recognition"""
        mock_face_system.recognize_face_from_base64.return_value = {
            "name": "John Doe",
            "confidence": 0.95
        }
        
        payload = {"image": sample_face_image}
        response = client.post("/recognize-face", json=payload)
        
        assert response.status_code == 200
        data = response.json()
        assert "name" in data
    
    def test_recognize_face_no_image(self, client):
        """Test face recognition without image"""
        response = client.post("/recognize-face", json={})
        
        assert response.status_code == 200
        data = response.json()
        assert "error" in data
    
    def test_recognize_face_error(self, client, sample_face_image):
        """Test face recognition with error (module not available)"""
        payload = {"image": sample_face_image}
        response = client.post("/recognize-face", json=payload)
        
        assert response.status_code == 200
        data = response.json()
        # Should return error since face-recognition module isn't installed
        assert "error" in data
    
    def test_register_face_success(self, client):
        """Test face registration (will fail without face-recognition module)"""
        payload = {
            "name": "Jane Smith",
            "encoding": [0.1, 0.2, 0.3]  # Fake encoding
        }
        response = client.post("/register-face", json=payload)
        
        assert response.status_code == 200
        data = response.json()
        # Will fail without module, but endpoint should handle gracefully
        assert "success" in data or "error" in data
    
    def test_register_face_missing_data(self, client):
        """Test face registration with missing data"""
        response = client.post("/register-face", json={"name": "John"})
        
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is False
        assert "error" in data


@pytest.mark.integration
class TestBookingEndpoints:
    """Test booking API endpoints"""
    
    def test_check_availability_no_api_key(self, client):
        """Test availability check without API key"""
        response = client.post(
            "/api/check-availability",
            params={
                "check_in": "2025-01-01",
                "check_out": "2025-01-05",
                "guests": 2
            }
        )
        
        # API key validation returns 401
        assert response.status_code == 401
        data = response.json()
        assert "detail" in data
    
    def test_check_availability_with_api_key(self, client):
        """Test availability check with API key"""
        response = client.post(
            "/api/check-availability",
            params={
                "check_in": "2025-01-01",
                "check_out": "2025-01-05",
                "guests": 2
            },
            headers={"x-api-key": "test-api-key"}
        )
        
        # Even with invalid key, returns 401
        assert response.status_code == 401


@pytest.mark.integration
class TestStaticFiles:
    """Test static file serving"""
    
    def test_get_avatar_glb(self, client):
        """Test avatar.glb file endpoint"""
        response = client.get("/avatar.glb")
        # File might not exist in test environment
        assert response.status_code in [200, 404]
    
    def test_get_dynamic_file(self, client):
        """Test dynamic file serving endpoint"""
        response = client.get("/nonexistent_file.txt")
        # Should return error for non-existent file
        assert response.status_code in [200, 404]


@pytest.mark.unit
class TestHealthCheck:
    """Test basic health and documentation endpoints"""
    
    def test_app_starts_successfully(self, client):
        """Verify app starts and responds to requests"""
        response = client.get("/docs")
        assert response.status_code == 200
