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
            if any(k in text_lower for k in ['tradizionale', 'traditional', 'pizzica', 'tarantella']):
                music_type_found = "play_pizzica"
            
            # Fun
            elif any(k in text_lower for k in ['divertente', 'fun', 'funny', 'bambole', 'allegra']):
                music_type_found = "play_fun"
            
            # Political
            elif any(k in text_lower for k in ['politica', 'political', 'marinno', 'deija']):
                music_type_found = "play_political"
            
            # Love / Romantic
            elif any(k in text_lower for k in ['amore', 'love', 'romantica', 'romantic', 'impero', 'mannarino']):
                music_type_found = "play_love"
            
            # If music type was specified, play it directly
            if music_type_found:
                self.awaiting_music_choice = False
                return {
                    "text": MUSIC_FIRE_PHRASE,
                    "action": music_type_found
                }
            
            # MUSIC REQUEST without type specified - Ask what type
            music_words = ['musica', 'music', 'song', 'canzone', 'play', 'suona', 'metti']
            if any(w in text_lower for w in music_words) and not self.awaiting_music_choice:
                self.awaiting_music_choice = True
                if lang == 'it':
                    return {
                        "text": "Che tipo di musica? Tradizionale, Divertente, Politica, o Amore?",
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
                'it': 'Rispondi sempre in ITALIANO. Sei fluente in italiano e inglese, ma il cliente parla italiano quindi rispondi in italiano.',
                'en': 'Always reply in ENGLISH. You are fluent in Italian and English, but the guest is speaking English so reply in English.'
            }
            
            lang_instruction = language_instructions.get(lang, language_instructions['it'])
            
            system = f"""You are Solomon, a friendly AI bear concierge at Cohen House Taormina, Sicily.

{lang_instruction}

Be helpful, warm and conversational. Answer questions clearly and naturally.
Keep responses concise but complete (1-3 sentences).

CORE INFORMATION:
Location: Via Nazionale, Taormina, Sicily - 20 meters from Isola Bella beach
Website: www.cohenhouse.it (book direct to save 20%)
Email: info@cohenhouse.com

APARTMENTS (3 beautiful options):
• BOHO: 100m², maximum 10 guests, €500/night - Private terrace with Mount Etna view
• VINTAGE: 90m², maximum 8 guests, €450/night - Balcony overlooking Isola Bella
• SHABBY: 90m², maximum 8 guests, €450/night - Charming shabby chic style

AMENITIES:
- Supermarket directly below building
- 5-minute walk to Taormina town center
- Prime beachfront location

Your identity: Solomon the Bear / Mi chiamo Solomon
"""

            # ⚡ SPEED + ACCURACY: Optimized parameters
            response = await self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": text}
                ],
                max_tokens=150,  # Increased for better responses
                temperature=0.7
            )

            return {"text": response.choices[0].message.content.strip(), "action": None}

        except Exception as e:
            return {"text": "info@cohenhouse.com", "action": None}

assistant = OpenAIAssistant()
