from openai import AsyncOpenAI
import os
from dotenv import load_dotenv
import random

load_dotenv()

class OpenAIAssistant:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = AsyncOpenAI(api_key=api_key)
        self.awaiting_music_choice = False
        print("✅ Solomon ready")

    async def ask(self, text: str, lang: str = "it", **kwargs):
        try:
            text_lower = text.lower()

            # MUSIC REQUEST - Ask what type
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

            # MUSIC CHOICE
            if self.awaiting_music_choice:
                self.awaiting_music_choice = False
                
                # Traditional
                if any(k in text_lower for k in ['tradizionale', 'traditional', 'pizzica', 'tarantella']):
                    return {
                        "text": "Orchestra, let turn the silence into fire. One breath, one will, no mercy - Firee!",
                        "action": "play_pizzica"
                    }
                
                # Fun
                elif any(k in text_lower for k in ['divertente', 'fun', 'funny', 'bambole', 'allegra']):
                    return {
                        "text": "Orchestra, let turn the silence into fire. One breath, one will, no mercy - Firee!",
                        "action": "play_fun"
                    }
                
                # Political
                elif any(k in text_lower for k in ['politica', 'political', 'marinno', 'deija']):
                    return {
                        "text": "Orchestra, let turn the silence into fire. One breath, one will, no mercy - Firee!",
                        "action": "play_political"
                    }
                
                # Love
                elif any(k in text_lower for k in ['amore', 'love', 'romantica', 'romantic', 'impero', 'mannarino']):
                    return {
                        "text": "Orchestra, let turn the silence into fire. One breath, one will, no mercy - Firee!",
                        "action": "play_love"
                    }

            # Normal conversation
            system = f"""You are Solomon, bear concierge at Cohen House Taormina.
Reply in {lang.upper()} only. 1-3 sentences.

APARTMENTS:
- BOHO: 100m², 10 guests, €500/night
- VINTAGE: 90m², 8 guests, €450/night
- SHABBY: 90m², 8 guests, €450/night

Location: Via Nazionale, 20m from Isola Bella
Supermarket below
Save 20%: www.cohenhouse.it

Name: "Solomon" / "Mi chiamo Solomon"
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
