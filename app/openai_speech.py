from openai import AsyncOpenAI
import os
from dotenv import load_dotenv
import re
from app.audio_filter import preprocess_audio

load_dotenv()

# Italian language detection keywords - EXPANDED for perfect recognition
ITALIAN_INDICATORS = [
    # Common greetings
    'ciao', 'buongiorno', 'buonasera', 'salve', 'buonanotte',
    # Questions
    'dove', 'quanto', 'costa', 'come', 'che', 'cosa', 'quando', 'perché', 'chi',
    # Common verbs
    'sei', 'sono', 'hai', 'ho', 'vuoi', 'voglio', 'posso', 'puoi',
    # Common words
    'grazie', 'prego', 'scusa', 'mi', 'chiamo', 'per', 'con', 'ma', 'e', 'o',
    # Location/apartment related
    'appartamento', 'camera', 'spiaggia', 'mare', 'vicino', 'lontano',
    # Numbers
    'uno', 'due', 'tre', 'quattro', 'cinque',
    # Common phrases
    'va bene', 'non', 'si', 'no', 'forse', 'anche'
]

# English indicators for contrast
ENGLISH_INDICATORS = [
    'hello', 'hi', 'hey', 'good', 'morning', 'evening', 'night',
    'where', 'what', 'how', 'when', 'why', 'who', 'which',
    'is', 'are', 'can', 'do', 'does', 'have', 'has', 'want', 'need',
    'the', 'a', 'an', 'this', 'that', 'these', 'those',
    'apartment', 'room', 'beach', 'sea', 'near', 'far',
    'thank', 'please', 'sorry', 'yes', 'no', 'maybe'
]

class OpenAISpeech:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = AsyncOpenAI(api_key=api_key) if api_key else None
        print("✅ Speech ready" if self.client else "⚠️ No API key")

    async def transcribe_audio(self, audio_file):
        if not self.client:
            return None, None

        try:
            # ⚡ OPTIMIZATION: Use prompt for faster, more accurate transcription
            transcript = await self.client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="json",  # ⚡ Changed from verbose_json for faster response
                temperature=0.0,
                    prompt="Cohen House, Taormina, Sicily, apartment, BOHO, VINTAGE, SHABBY"  # Context for better accuracy
                )
            
            # Cleanup
            import os
            try:
                if 'cleaned_path' in locals() and os.path.exists(cleaned_path):
                    os.remove(cleaned_path)
            except:
                pass

            text = transcript.text.strip()
            
            # Ignore very short or nonsensical transcriptions
            # Block only VERY short noise
            if len(text) < 3:
                print(f"❌ Text too short: {text}")
                return None, None
            
            # Allow Latin + accented characters (Italian, French, Spanish, etc.)
            # Block only problematic scripts (emoji, Chinese, etc.)
            if re.search(r'[𐀀-􏿿一-鿿]', text):
                print(f"❌ Non-Latin blocked")
                return None, None
            
            # Block YouTube spam
            # Load comprehensive spam database
            import json
            try:
                with open("app/spam_database.json", "r", encoding="utf-8") as f:
                    spam_db = json.load(f)
                    spam = []
                    for category in spam_db.values():
                        spam.extend(category)
            except:
                spam = ["subscribe", "abone", "дякую"]

            if sum(s in text.lower() for s in spam) >= 2:  # Require 2+ spam words
                print(f"❌ Spam blocked")
                return None, None
            
            # Too short or too long
            if len(text) < 4 or len(text.split()) > 15:
                return None, None

            # ⚡ PERFECT LANGUAGE DETECTION: Score-based system for accuracy
            text_words = text.lower().split()
            
            # Count matches for each language
            italian_score = sum(1 for word in text_words if word in ITALIAN_INDICATORS)
            english_score = sum(1 for word in text_words if word in ENGLISH_INDICATORS)
            
            # Determine language with confidence
            if italian_score > english_score:
                lang = 'it'
                confidence = 'high' if italian_score >= 2 else 'medium'
            elif english_score > italian_score:
                lang = 'en'
                confidence = 'high' if english_score >= 2 else 'medium'
            else:
                # Default to Italian for Cohen House (most common)
                lang = 'it'
                confidence = 'low'
            
            print(f"✅ [{lang.upper()}:{confidence}] {text}")
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
