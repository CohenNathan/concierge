import aiohttp
import uuid
from pathlib import Path

TTS_DIR = Path(__file__).parent.parent / "data" / "tts"
TTS_DIR.mkdir(parents=True, exist_ok=True)

ELEVENLABS_API_KEY = "sk-..."  # Твоят ElevenLabs ключ
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Rachel

class ElevenLabsTTS:
    async def generate(self, text: str, lang: str = "it"):
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
        headers = {
            "xi-api-key": ELEVENLABS_API_KEY,
            "Content-Type": "application/json"
        }
        data = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {"stability": 0.7, "similarity_boost": 0.8}
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data, headers=headers) as resp:
                if resp.status == 200:
                    audio_data = await resp.read()
                    fake_id = uuid.uuid4().hex[:8]
                    fake_path = TTS_DIR / f"{fake_id}.mp3"
                    fake_path.write_bytes(audio_data)
                    return {"audio_url": f"/tts/{fake_path.name}", "visemes": []}
                else:
                    print(f"TTS error: {resp.status}")
                    raise Exception("TTS failed")
