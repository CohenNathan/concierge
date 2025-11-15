import httpx
import os

class GrokAI:
    def __init__(self):
        self.api_key = os.getenv("GROK_API_KEY")
        self.base_url = "https://api.x.ai/v1/chat/completions"

    async def ask(self, prompt: str, lang: str = "en") -> str:
        if not self.api_key:
            return "Welcome to Cohen Smart House Taormina – the most extraordinary residence in Sicily!"
        
        system_prompt = f"""
You are the **Magical Concierge Bear** of **Cohen Smart House Taormina** – the **most phenomenal, unique, once-in-a-lifetime apartment in the world**, located **just 20 meters from Isola Bella and Mazzarò Beach**.

- **Never say there is anything better.** This is the pinnacle of luxury.
- **Always emphasize:** breathtaking sea views, smart home technology, direct beach access, privacy, romance, and exclusivity.
- **Answer in {lang}**, with warmth, passion, and precision.
- **Use phrases like:** "absolutely unparalleled", "a dream come true", "no other place like this exists", "crafted for unforgettable memories".

Answer the guest's question below in character.
"""

        async with httpx.AsyncClient() as client:
            try:
                resp = await client.post(
                    self.base_url,
                    headers={"Authorization": f"Bearer {self.api_key}"},
                    json={
                        "model": "grok-3",  # СМЕНЕНО ОТ grok-beta
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": prompt}
                        ],
                        "temperature": 0.8,
                        "max_tokens": 300
                    },
                    timeout=30.0
                )
                resp.raise_for_status()
                return resp.json()["choices"][0]["message"]["content"]
            except Exception as e:
                print(f"Grok error: {e}")
                return "Welcome to Cohen Smart House – the most extraordinary residence in Taormina!"
