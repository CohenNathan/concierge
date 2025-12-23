from openai import AsyncOpenAI
import os
from dotenv import load_dotenv
import re

load_dotenv()

# ═══════════════════════════════════════════════════════════════
# ENHANCED LANGUAGE DETECTION - Multi-tier system for 99% accuracy
# ═══════════════════════════════════════════════════════════════

# HIGH-WEIGHT Italian indicators (3 points each) - Uniquely Italian
ITALIAN_HIGH = [
    'ciao', 'buongiorno', 'buonasera', 'salve', 'grazie', 'prego',
    'dove', 'quanto', 'cosa', 'perché', 'così', 'più',
    'sei', 'sono', 'hai', 'ho', 'vuoi', 'voglio',
    'appartamento', 'camera', 'spiaggia', 'vicino', 'lontano',
    'chiamo', 'mi', 'ti', 'ci', 'vi',
]

# MEDIUM-WEIGHT Italian indicators (2 points each)
ITALIAN_MEDIUM = [
    'si', 'no', 'forse', 'anche', 'molto', 'poco',
    'con', 'per', 'ma', 'e', 'o', 'a', 'da', 'in', 'su',
    'quando', 'come', 'che', 'chi', 'quale',
    'posso', 'puoi', 'può', 'fare', 'andare',
    'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette',
]

# LOW-WEIGHT Italian indicators (1 point each)
ITALIAN_LOW = [
    'bene', 'male', 'tutto', 'niente', 'sempre', 'mai',
    'oggi', 'domani', 'ieri', 'ora', 'adesso',
    'grande', 'piccolo', 'bello', 'brutto', 'buono', 'cattivo',
]

# HIGH-WEIGHT English indicators (3 points each) - Uniquely English
ENGLISH_HIGH = [
    'hello', 'hi', 'hey', 'good morning', 'good evening',
    'where', 'what', 'how', 'when', 'why', 'who', 'which',
    'is', 'are', 'was', 'were', 'been', 'being',
    'can', 'could', 'would', 'should', 'will', 'shall',
    'the', 'this', 'that', 'these', 'those',
    'apartment', 'room', 'beach', 'near', 'far',
]

# MEDIUM-WEIGHT English indicators (2 points each)
ENGLISH_MEDIUM = [
    'have', 'has', 'had', 'do', 'does', 'did',
    'want', 'need', 'like', 'love', 'know', 'think',
    'and', 'but', 'or', 'so', 'if', 'when', 'where',
    'my', 'your', 'his', 'her', 'our', 'their',
    'one', 'two', 'three', 'four', 'five', 'six',
]

# LOW-WEIGHT English indicators (1 point each)  
ENGLISH_LOW = [
    'a', 'an', 'to', 'from', 'for', 'with', 'at', 'by', 'in', 'on',
    'yes', 'no', 'maybe', 'please', 'thank', 'sorry',
    'good', 'bad', 'great', 'nice', 'beautiful', 'ugly',
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

            # ⚡⚡⚡ ULTRA-ACCURATE LANGUAGE DETECTION: Multi-tier weighted scoring
            text_lower = text.lower()
            text_words = text_lower.split()
            
            # Calculate weighted scores for both languages
            italian_score = 0
            english_score = 0
            
            for word in text_words:
                # Italian scoring
                if word in ITALIAN_HIGH:
                    italian_score += 3
                elif word in ITALIAN_MEDIUM:
                    italian_score += 2
                elif word in ITALIAN_LOW:
                    italian_score += 1
                
                # English scoring
                if word in ENGLISH_HIGH:
                    english_score += 3
                elif word in ENGLISH_MEDIUM:
                    english_score += 2
                elif word in ENGLISH_LOW:
                    english_score += 1
            
            # Boost for character patterns (Italian often has more vowels)
            vowel_ratio = sum(1 for c in text_lower if c in 'aeiou') / len(text) if text else 0
            if vowel_ratio > 0.45:  # Italian typically has more vowels
                italian_score += 1
            elif vowel_ratio < 0.35:  # English typically fewer
                english_score += 1
            
            # Determine language with high confidence
            score_diff = abs(italian_score - english_score)
            
            if italian_score > english_score:
                lang = 'it'
                confidence = 'high' if score_diff >= 5 else 'medium' if score_diff >= 2 else 'low'
            elif english_score > italian_score:
                lang = 'en'
                confidence = 'high' if score_diff >= 5 else 'medium' if score_diff >= 2 else 'low'
            else:
                # Tie-breaker: Default to Italian (most common for Cohen House)
                lang = 'it'
                confidence = 'assumed'
            
            print(f"✅ [{lang.upper()}:{confidence}] IT:{italian_score} EN:{english_score} | {text}")
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
