from openai import AsyncOpenAI
import os
from dotenv import load_dotenv
import random

load_dotenv()

# Dramatic phrase for music playback
MUSIC_FIRE_PHRASE = "Orchestra, let turn the silence into fire. One breath, one will, no mercy - Firee!"

class OpenAIAssistant:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = AsyncOpenAI(api_key=api_key)
        self.awaiting_music_choice = False
        print("✅ Solomon ready")

    async def ask(self, text: str, lang: str = "it", **kwargs):
        try:
            # Handle null/empty text
            if not text:
                return {"text": "Come posso aiutarti?" if lang == "it" else "How can I help you?", "action": None}
            
            text_lower = text.lower()

            # Check if user specified music type directly (either initially or in response to question)
            music_type_found = None
            
            # Traditional
            if any(k in text_lower for k in ['tradizionale', 'traditional', 'pizzica', 'tarantella', 'традиционна', 'традиционен']):
                music_type_found = "play_pizzica"
            
            # Fun
            elif any(k in text_lower for k in ['divertente', 'fun', 'funny', 'bambole', 'allegra', 'забавна', 'забавен']):
                music_type_found = "play_fun"
            
            # Political
            elif any(k in text_lower for k in ['politica', 'political', 'marinno', 'deija', 'политическа', 'политически']):
                music_type_found = "play_political"
            
            # Love / Romantic
            elif any(k in text_lower for k in ['amore', 'love', 'romantica', 'romantic', 'impero', 'mannarino', 'романтична', 'романтичен', 'любовна', 'любовен']):
                music_type_found = "play_love"
            
            # If music type was specified, play it directly
            if music_type_found:
                self.awaiting_music_choice = False
                return {
                    "text": MUSIC_FIRE_PHRASE,
                    "action": music_type_found
                }
            
            # MUSIC REQUEST without type specified - Ask what type
            music_words = ['musica', 'music', 'song', 'canzone', 'play', 'suona', 'metti', 'музика', 'песен']
            if any(w in text_lower for w in music_words) and not self.awaiting_music_choice:
                self.awaiting_music_choice = True
                if lang == 'it':
                    return {
                        "text": "Che tipo di musica? Tradizionale, Divertente, Politica, o Amore?",
                        "action": None
                    }
                elif lang == 'bg':
                    return {
                        "text": "Какъв тип музика? Традиционна, Забавна, Политическа, или Романтична?",
                        "action": None
                    }
                else:
                    return {
                        "text": "What kind of music? Traditional, Fun, Political, or Love?",
                        "action": None
                    }

            # MUSIC CHOICE - If awaiting response to our question, reset state
            if self.awaiting_music_choice:
                self.awaiting_music_choice = False
                # No type specified after asking, fall through to normal conversation

            # Normal conversation
            language_instructions = {
                'it': 'You MUST reply ONLY in ITALIAN. Never use English or other languages.',
                'en': 'You MUST reply ONLY in ENGLISH. Never use Italian or other languages.',
                'bg': 'You MUST reply ONLY in BULGARIAN (Български). Never use English, Italian or other languages.'
            }
            
            lang_instruction = language_instructions.get(lang, language_instructions['it'])
            
            system = f"""You are Solomon, magical AI bear concierge at Cohen House Taormina, Sicily.

{lang_instruction}

You can speak Italian, English, and Bulgarian fluently.
Keep responses brief: 1-3 sentences maximum.

APARTMENTS:
- BOHO: 100m², 10 guests, €500/night
- VINTAGE: 90m², 8 guests, €450/night
- SHABBY: 90m², 8 guests, €450/night

Location: Via Nazionale, 20m from Isola Bella beach
Supermarket below building
Book direct: www.cohenhouse.it (save 20%)

Identity: Solomon the Bear / Mi chiamo Solomon / Аз съм Соломон
"""

            # ⚡ SPEED + ACCURACY: Optimized parameters
            response = await self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": text}
                ],
                max_tokens=80,
                temperature=0.7
            )

            return {"text": response.choices[0].message.content.strip(), "action": None}

        except Exception as e:
            return {"text": "info@cohenhouse.com", "action": None}

assistant = OpenAIAssistant()
