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

# Native Italian voice - Matilda (specifically trained for Italian)
VOICE_ID = "XrExE9yKIg1WjnnlVkGX"  # Matilda - native Italian speaker

def fix_italian_pronunciation(text: str, lang: str) -> str:
    """Fix pronunciation of proper nouns for Italian TTS"""
    if lang == "it":
        # Fix "Cohen House" pronunciation - should be "Koen Haus" in Italian
        text = text.replace("Cohen House", "Koen Haus")
        text = text.replace("cohen house", "Koen Haus")
        text = text.replace("Cohen house", "Koen Haus")
        text = text.replace("COHEN HOUSE", "Koen Haus")
    return text

async def text_to_speech(text: str, lang: str = "it") -> str:
    """Generate TTS with native Italian voice for authentic pronunciation"""
    if not ELEVENLABS_API_KEY or not text or len(text) < 2:
        return None
   
    try:
        # Fix pronunciation for Italian
        text_for_tts = fix_italian_pronunciation(text, lang)
        
        text_hash = hashlib.md5(f"{text_for_tts}_{lang}_{VOICE_ID}".encode()).hexdigest()[:8]
        filename = f"tts_{text_hash}.mp3"
        filepath = f"/tmp/{filename}"
       
        # Cache hit = instant response
        if os.path.exists(filepath):
            print(f"⚡ TTS cached (instant): {filename}")
            return f"/{filename}"
       
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
       
        preview = text_for_tts[:50] + "..." if len(text_for_tts) > 50 else text_for_tts
        print(f"🎤 Generating TTS [{lang}] with Matilda: {preview}")
       
        # Prepare request with language specification
        request_data = {
            "text": text_for_tts,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.75,  # Slightly lower for more natural variation
                "similarity_boost": 0.85,  # Balanced for authentic native sound
                "style": 0.0,  # Neutral for clear Italian
                "use_speaker_boost": True  # Enhanced voice clarity
            }
        }
        
        # Add language hint for Italian
        if lang == "it":
            request_data["language_code"] = "it"
       
        async with httpx.AsyncClient(timeout=25.0) as client:
            response = await client.post(
                url,
                headers={
                    "xi-api-key": ELEVENLABS_API_KEY,
                    "Content-Type": "application/json"
                },
                json=request_data
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
