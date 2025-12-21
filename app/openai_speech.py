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
            # Use explicit language hints for better detection
            transcript = await self.client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="verbose_json",
                temperature=0.0,  # Lower for more accurate transcription
                language=None  # Auto-detect but we'll improve detection below
            )

            text = transcript.text.strip()
            detected_lang = transcript.language.lower() if hasattr(transcript, 'language') else None
            
            # Block EVERYTHING except Latin alphabet
            if re.search(r'[^\x00-\x7F]', text):
                print(f"❌ Non-Latin blocked")
                return None, None
            
            # Block only obvious YouTube spam + generic endings
            spam_patterns = [
                'subscribe to my channel',
                'like and subscribe', 
                'check out my channel',
                'link in description',
                'smash that like button',
                'thanks for watching',
                'thank you for watching',
                'see you next time',
                'don\'t forget to subscribe'
            ]
            if any(s in text.lower() for s in spam_patterns):
                print(f"❌ Spam blocked: {text}")
                return None, None
            
            # Too short or too long (more relaxed - allow up to 30 words)
            if len(text) < 2 or len(text.split()) > 30:
                return None, None

            # Improved language detection with better Italian coverage
            # Check for Italian-specific words/patterns
            italian_indicators = ['ciao', 'grazie', 'buongiorno', 'buonasera', 'come stai', 'va bene', 
                                 'appartamento', 'prezzo', 'dove', 'quando', 'cosa', 'chi', 'perché',
                                 'mi chiamo', 'sono', 'sei', 'è', 'parli', 'italiano', 'senti', 
                                 'quanto', 'costa', 'dista', 'lontano', 'vicino', 'bella', 'spiaggia',
                                 'mare', 'casa', 'come', 'molto', 'poco', 'bene', 'male']
            
            # Check for English-specific words/patterns
            english_indicators = ['hello', 'thanks', 'good morning', 'good evening', 'how are you',
                                 'apartment', 'price', 'where', 'when', 'what', 'who', 'why',
                                 'my name', 'i am', 'you are', 'speak', 'english', 'do you',
                                 'how much', 'how far', 'away', 'near', 'beach', 'sea', 'house',
                                 'get to', 'from', 'very', 'good', 'bad', 'tell me', 'about']
            
            text_lower = text.lower()
            italian_count = sum(1 for word in italian_indicators if word in text_lower)
            english_count = sum(1 for word in english_indicators if word in text_lower)
            
            # Determine language based on indicators or Whisper detection
            if italian_count > english_count:
                lang = 'it'
            elif english_count > italian_count:
                lang = 'en'
            elif detected_lang in ['it', 'italian', 'ita']:
                lang = 'it'
            elif detected_lang in ['en', 'english', 'eng']:
                lang = 'en'
            else:
                # Default to Italian as it's the primary language
                lang = 'it'
            
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
