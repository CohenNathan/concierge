from openai import AsyncOpenAI
import os
from dotenv import load_dotenv
import random

load_dotenv()

class OpenAIAssistant:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = AsyncOpenAI(api_key=api_key)
        print("✅ Solomon ready")

    async def ask(self, text: str, lang: str = "it", **kwargs):
        try:
            text_lower = text.lower()

            # MUSIC TRIGGER with 3 options
            if any(k in text_lower for k in ['musica', 'music', 'spotify', 'canzone', 'song', 'suona', 'play', 'metti']):
                # Traditional
                if any(k in text_lower for k in ['pizzica', 'tradizionale', 'traditional', 'tarantella', 'salento']):
                    phrases = [
                        "The ancient rhythm awakens... PIZZICA DI SAN VITO!",
                        "Salento spirit rising... Orchestra – PIZZICA!"
                    ]
                    return {"text": random.choice(phrases), "action": "play_pizzica"}

                # Fun
                if any(k in text_lower for k in ['divertente', 'fun', 'bambole', 'allegra']):
                    phrases = [
                        "Chaos incoming! VOGLIAMO LE BAMBOLE!",
                        "Madness begins... Vogliamo le bambole!"
                    ]
                    return {"text": random.choice(phrases), "action": "play_bambole"}

                # Default – ask and open Spotify
                phrases = [
                    "Orchestra awaits your command. What kind of music? Traditional, fun, or your choice on Spotify?",
                    "The stage is set. Tell me your mood – opening Spotify for you."
                ]
                return {"text": random.choice(phrases), "action": "open_spotify"}

            # Normal responses with EXACT facts
            system = f"""You are Solomon, magical AI bear concierge at Cohen House Taormina.

REPLY IN {lang.upper()} ONLY! Be brief (1-3 sentences).

EXACT FACTS:
APARTMENTS:
- BOHO: 100m², 10 guests, €500/night, bohemian, terrace with Etna view
- VINTAGE: 90m², 8 guests, €450/night, baroque, balcony over Isola Bella
- SHABBY: 90m², 8 guests, €450/night, shabby chic, pastel

LOCATION: Via Nazionale, 20m from Isola Bella
SUPERMARKET: Below Cohen House
BOOKING: Save 20-25% at www.cohenhouse.it

NAME:
- IT: "Mi chiamo Solomon!"
- EN: "I'm Solomon!"
"""

            # ⚡ OPTIMIZATION: Reduced max_tokens to 80 and temperature to 0.3 for faster responses
            response = await self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": text}
                ],
                max_tokens=80,  # Reduced from 120
                temperature=0.3  # Reduced from 0.5 for faster, more deterministic responses
            )

            return {"text": response.choices[0].message.content.strip(), "action": None}

        except Exception as e:
            return {"text": "info@cohenhouse.com", "action": None}

assistant = OpenAIAssistant()
