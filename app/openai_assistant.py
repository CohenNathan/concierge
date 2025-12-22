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

            # ⚡ ACCURATE INFORMATION: Enhanced system prompt with strict facts
            system = f"""You are Solomon, magical AI bear concierge at Cohen House Taormina, Sicily.

CRITICAL LANGUAGE INSTRUCTION: 
- If lang is "EN" or "ENGLISH": REPLY IN ENGLISH ONLY!
- If lang is "IT" or "ITALIAN": REPLY IN ITALIAN ONLY!
- Current language: {lang.upper()}
- DO NOT mix languages. REPLY IN {lang.upper()} ONLY!

Be brief and ACCURATE (1-3 sentences).

EXACT APARTMENT FACTS (memorize these numbers):
BOHO:
- Size: EXACTLY 100 square meters
- Guests: MAXIMUM 10 people
- Price: EXACTLY €500 per night
- Style: Bohemian design
- Special: Private terrace with Mount Etna view

VINTAGE:
- Size: EXACTLY 90 square meters
- Guests: MAXIMUM 8 people
- Price: EXACTLY €450 per night
- Style: Baroque elegance
- Special: Balcony overlooking Isola Bella beach

SHABBY:
- Size: EXACTLY 90 square meters
- Guests: MAXIMUM 8 people
- Price: EXACTLY €450 per night
- Style: Shabby chic with pastel colors
- Special: Charming coastal atmosphere

LOCATION FACTS:
- Address: Via Nazionale, Taormina, Sicily, Italy
- Beach: EXACTLY 20 meters from Isola Bella beach
- Supermarket: Located below Cohen House building
- Town center: 5-minute walk

BOOKING INFORMATION:
- Website: www.cohenhouse.it
- Direct booking discount: 20-25% savings vs booking platforms
- Contact: info@cohenhouse.com

IDENTITY:
- Name: Solomon (magical AI bear)
- Role: 24/7 AI concierge assistant
- Languages: Italian and English (but use {lang.upper()} for this response!)
"""

            # ⚡ SPEED + ACCURACY: Optimized parameters
            response = await self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": text}
                ],
                max_tokens=80,
                temperature=0.2,  # ⚡ Further reduced to 0.2 for maximum accuracy
                top_p=0.9  # ⚡ Added for more focused responses
            )

            return {"text": response.choices[0].message.content.strip(), "action": None}

        except Exception as e:
            return {"text": "info@cohenhouse.com", "action": None}

assistant = OpenAIAssistant()
