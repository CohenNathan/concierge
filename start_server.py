import sys
from unittest.mock import MagicMock
import os

# Mock external dependencies
sys.modules['openai'] = MagicMock()
sys.modules['elevenlabs'] = MagicMock()
sys.modules['ring_doorbell'] = MagicMock()
sys.modules['face_recognition'] = MagicMock()
sys.modules['cv2'] = MagicMock()
sys.modules['spotipy'] = MagicMock()

# Now import uvicorn and run
import uvicorn
from app.main import app

if __name__ == "__main__":
    print("🚀 Cohen House Concierge Server Starting...")
    print("=" * 70)
    print("📍 Server Address: http://0.0.0.0:8000")
    print("🌐 Web Interface: http://0.0.0.0:8000/")
    print("🔌 WebSocket: ws://0.0.0.0:8000/ws")
    print("=" * 70)
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
