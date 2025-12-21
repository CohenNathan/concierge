from openai import AsyncOpenAI
import os
from dotenv import load_dotenv
import re

load_dotenv()

class OpenAISpeech:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = AsyncOpenAI(api_key=api_key) if api_key else None
        print("✅ Speech ready" if self.client else "⚠️ No API key")

    async def transcribe_audio(self, audio_file):
        if not self.client:
            return None, None

        try:
            transcript = await self.client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="verbose_json",
                temperature=0.0
            )

            text = transcript.text.strip()
            
            # Block EVERYTHING except Latin alphabet
            if re.search(r'[^\x00-\x7F]', text):
                print(f"❌ Non-Latin blocked")
                return None, None
            
            # Block YouTube spam
            spam = ['subscribe', 'thank you', 'share', 'friends', 'social media', 'channel', 'video']
            if any(s in text.lower() for s in spam):
                print(f"❌ Spam blocked")
                return None, None
            
            # Too short or too long
            if len(text) < 4 or len(text.split()) > 15:
                return None, None

            lang = 'it' if transcript.language.lower() in ['it', 'italian'] else 'en'
            print(f"✅ [{lang}] {text}")
            return text, lang

        except Exception as e:
            print(f"❌ {e}")
            return None, None

_speech_client = None

def get_speech_client():
    global _speech_client
    if _speech_client is None:
        _speech_client = OpenAISpeech()
    return _speech_client
