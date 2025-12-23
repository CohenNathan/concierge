from openai import AsyncOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class OpenAIAssistant:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = AsyncOpenAI(api_key=api_key)
        print("✅ Solomon ready")

    async def ask(self, text: str, lang: str = "it", **kwargs):
        try:
            text_lower = text.lower()

            # Check for music type keywords FIRST
            if any(k in text_lower for k in ['traditional', 'tradizionale', 'pizzica']):
                return {
                    "text": "Orchestra... turn silence into fire. One breath, one will - no mercy. FIRE!",
                    "action": "play_pizzica"
                }
            
            if any(k in text_lower for k in ['fun', 'divertente', 'funny', 'bambole']):
                return {
                    "text": "Orchestra... turn silence into fire. One breath, one will - no mercy. FIRE!",
                    "action": "play_fun"
                }
            
            if any(k in text_lower for k in ['political', 'politica', 'marinno']):
                return {
                    "text": "Orchestra... turn silence into fire. One breath, one will - no mercy. FIRE!",
                    "action": "play_political"
                }
            
            if any(k in text_lower for k in ['love', 'amore', 'romantic', 'mannarino']):
                return {
                    "text": "Orchestra... turn silence into fire. One breath, one will - no mercy. FIRE!",
                    "action": "play_love"
                }

            # Generic music request - ask for type
            if any(k in text_lower for k in ['music', 'musica', 'song', 'canzone']):
                if lang == 'it':
                    return {
                        "text": "Che musica? Tradizionale, Divertente, Politica, o Amore?",
                        "action": None
                    }
                else:
                    return {
                        "text": "What music? Traditional, Fun, Political, or Love?",
                        "action": None
                    }

            # Normal conversation
            system = f"""You are Solomon, bear concierge at Cohen House.
Reply in {lang.upper()} only. 1-2 sentences max.

BOHO: 100m², €500/night
VINTAGE: 90m², €450/night
SHABBY: 90m², €450/night

Via Nazionale, 20m from Isola Bella
www.cohenhouse.it

Name: "Solomon"
"""

            response = await self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": text}
                ],
                max_tokens=60,
                temperature=0.7
            )
            
            return {"text": response.choices[0].message.content.strip(), "action": None}
            
        except Exception as e:
            return {"text": "info@cohenhouse.com", "action": None}

assistant = OpenAIAssistant()
