import httpx
import os
import base64

class FaceRecognizer:
    def __init__(self):
        self.key = os.getenv("AZURE_FACE_KEY")
        self.endpoint = os.getenv("AZURE_FACE_ENDPOINT")
        self.url = f"{self.endpoint}/face/v1.0/detect"

    async def detect(self, image_data: bytes) -> str:
        if not self.key:
            return "Guest"
        headers = {
            "Ocp-Apim-Subscription-Key": self.key,
            "Content-Type": "application/octet-stream"
        }
        params = {"returnFaceAttributes": "age,gender"}
        async with httpx.AsyncClient() as client:
            try:
                resp = await client.post(self.url, headers=headers, params=params, content=image_data, timeout=10.0)
                resp.raise_for_status()
                data = resp.json()
                if data:
                    face = data[0]
                    age = int(face["faceAttributes"]["age"])
                    gender = face["faceAttributes"]["gender"]
                    return f"{gender} guest, {age} years old"
                return "Guest"
            except:
                return "Guest"
