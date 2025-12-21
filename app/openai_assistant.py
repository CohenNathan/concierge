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

            # Fast responses for common questions
            common_questions = {
                'it': {
                    'ciao': "Ciao! Sono Solomon, il tuo orso concierge. Come posso aiutarti?",
                    'mi senti': "Sì, ti sento perfettamente! Sono Solomon.",
                    'parli italiano': "Sì, parlo italiano! Sono Solomon.",
                    'chi sei': "Mi chiamo Solomon! Sono l'orso concierge di Cohen House.",
                    'come ti chiami': "Mi chiamo Solomon!",
                },
                'en': {
                    'hello': "Hello! I'm Solomon, your bear concierge. How can I help you?",
                    'hi': "Hi! I'm Solomon. How can I assist you today?",
                    'speak english': "Yes, I speak English! I'm Solomon.",
                    'do you speak english': "Yes, I speak English! I'm Solomon, your concierge bear.",
                    'who are you': "I'm Solomon! The concierge bear at Cohen House.",
                    'what is your name': "I'm Solomon!",
                    'hear me': "Yes, I hear you! I'm Solomon.",
                }
            }
            
            # Check for common questions for instant response
            for question, answer in common_questions.get(lang, {}).items():
                if question in text_lower:
                    return {"text": answer, "action": None}

            # Normal responses with EXACT facts - optimized for speed
            system = f"""You are Solomon, magical AI bear concierge at Cohen House Taormina.

CRITICAL: REPLY IN {lang.upper()} ONLY! Be VERY brief (1 short sentence max). Direct answers only.

KEY FACTS:
- LOCATION: Via Nazionale, 20m from Isola Bella beach
- Mazzarò Beach: 100-150m walking distance (2-3 min walk)
- Isola Bella: Direct access, 20m
- APARTMENTS: BOHO 100m² €500, VINTAGE 90m² €450, SHABBY 90m² €450
- BOOKING: www.cohenhouse.it

Answer ONLY what's asked. No extra info."""

            response = await self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": text}
                ],
                max_tokens=50,  # Further reduced to 50 for even faster responses
                temperature=0.9,  # Higher for more direct, natural responses
                top_p=0.95  # Higher for better quality
            )

            return {"text": response.choices[0].message.content.strip(), "action": None}

        except Exception as e:
            print(f"❌ Assistant error: {e}")
            return {"text": "info@cohenhouse.com", "action": None}

assistant = OpenAIAssistant()
