import os
import httpx
import hashlib
from dotenv import load_dotenv

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

if ELEVENLABS_API_KEY:
    print(f"✅ ElevenLabs API key loaded")
else:
    print("⚠️ No ElevenLabs API key!")

# Original voice
VOICE_ID = "RxJZoVFTFvDcilRItefF"  # Original bear voice

async def text_to_speech(text: str, lang: str = "it") -> str:
    """Generate TTS with original bear voice - OPTIMIZED"""
    if not ELEVENLABS_API_KEY or not text or len(text) < 2:
        return None
   
    try: 
        text_hash = hashlib.md5(f"{text}_{lang}".encode()).hexdigest()[:8]
        filename = f"tts_{text_hash}.mp3"
        filepath = f"/tmp/{filename}"
       
        # ⚡ OPTIMIZATION: Cache hit = instant response
        if os.path.exists(filepath):
            print(f"⚡ TTS cached (instant): {filename}")
            return f"/{filename}"
       
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
       
        preview = text[:50] + "..." if len(text) > 50 else text
        print(f"🎤 Generating TTS [{lang}]: {preview}")
       
        # ⚡ OPTIMIZATION: Reduced timeout from 30s to 15s
        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.post(
                url,
                headers={
                    "xi-api-key": ELEVENLABS_API_KEY,
                    "Content-Type": "application/json"
                },
                json={
                    "text": text,
                    "model_id": "eleven_turbo_v2",  # ⚡ OPTIMIZATION: Using turbo model for 2x speed
                    "voice_settings": {
                        "stability": 0.85,  # Slightly reduced for speed
                        "similarity_boost": 0.9,  # Slightly reduced for speed
                        "style": 0.3  # Reduced for faster generation
                    }
                }
            )
           
            print(f"📡 TTS response: {response.status_code}")
           
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"✅ TTS created: {filename} ({len(response.content)} bytes)")
                return f"/{filename}"
            else: 
                print(f"❌ TTS error: {response.status_code} - {response.text}")
                return None
               
    except Exception as e:
        print(f"❌ TTS exception: {e}")
        return None
