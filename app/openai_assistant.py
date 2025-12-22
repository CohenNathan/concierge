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

            # MUSIC TRIGGER with 3 options - DRAMATIC and COMMANDING tone
            if any(k in text_lower for k in ['musica', 'music', 'spotify', 'canzone', 'song', 'suona', 'play', 'metti']):
                # Traditional - EPIC and POWERFUL
                if any(k in text_lower for k in ['pizzica', 'tradizionale', 'traditional', 'tarantella', 'salento']):
                    phrases = [
                        "Orchestra! L'aria diventa fuoco! SUONATE! PIZZICA DI SAN VITO!",
                        "Soldiers of Salento, ARISE! The drums call you to destiny! PIZZICA!",
                        "Warriors! The ancient rhythm COMMANDS you! Into battle! PIZZICA DI SAN VITO!"
                    ]
                    return {"text": random.choice(phrases), "action": "play_pizzica"}

                # Fun - Still COMMANDING but with energy
                if any(k in text_lower for k in ['divertente', 'fun', 'bambole', 'allegra']):
                    phrases = [
                        "CHARGE! The madness begins! VOGLIAMO LE BAMBOLE!",
                        "Storm the gates! Nothing stops us! VOGLIAMO LE BAMBOLE!",
                        "FORWARD! Chaos is our ally! Vogliamo le bambole!"
                    ]
                    return {"text": random.choice(phrases), "action": "play_bambole"}

                # Default – COMMANDING tone
                phrases = [
                    "Orchestra stands ready! Choose your weapon: Traditional war drums, explosive chaos, or command Spotify yourself!",
                    "The battle awaits! Declare your music: Pizzica warriors, bambole madness, or take the Spotify throne!"
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
