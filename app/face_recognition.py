"""
Face Recognition for proactive greetings
"""
import asyncio
from pathlib import Path

class FaceRecognition:
    def __init__(self):
        self.known_faces = {}
        self.camera = None
        self.last_seen = {}
        
        # Known faces
        self.known_faces = {
            'nathan': 'Nathan',
            'guest': 'Guest'
        }
        
        print("✅ Face Recognition initialized")
    
    async def start_monitoring(self, on_face_detected):
        """Monitor camera for faces"""
        print("📹 Camera monitoring started (disabled for now)")
        
        # TODO: Implement actual camera monitoring with OpenCV
        # For now: disabled to avoid camera permission issues
        
        # Simulate: never detect faces unless explicitly triggered
        while True:
            await asyncio.sleep(60)  # Check every minute (but do nothing)
    
    async def stop(self):
        """Stop camera monitoring"""
        pass
