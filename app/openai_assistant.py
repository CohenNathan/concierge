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
            
            # RING DOORBELL - Nathan/Natan or Joanna inquiry
            if any(name in text_lower for name in ['nathan', 'natan', 'joanna', 'натан', 'джоана', 'джоанна']):
                if any(q in text_lower for q in ['home', 'here', 'дома', 'тук', 'къщи', 'casa', 'qui', 'è qui', 'c\'è']):
                    responses = {
                        'it': "Nathan e Joanna non sono in casa al momento, ma posso prendere un messaggio e glielo trasmetterò appena possibile.",
                        'en': "Nathan and Joanna are not home at the moment, but I can take a message and relay it to them as soon as possible.",
                        'bg': "Нейтън и Джоана не са в къщи в момента, но мога да приема съобщение и ще им го предам възможно най-скоро."
                    }
                    return {"text": responses.get(lang, responses['en']), "action": None}
            
            # WEBSITE OPENING TRIGGERS
            if any(k in text_lower for k in ['website', 'sito', 'уебсайт', 'web', 'cohen house', 'cohenhouse']):
                responses = {
                    'it': "Apro il sito di Cohen House! Ricorda: prenota sempre direttamente per risparmiare il 20-25% evitando le commissioni di Booking.com, Expedia e TripAdvisor.",
                    'en': "Opening Cohen House website! Remember: always book directly to save 20-25% by avoiding Booking.com, Expedia, and TripAdvisor commissions.",
                    'bg': "Отварям уебсайта на Cohen House! Помни: винаги резервирай директно, за да спестиш 20-25%, избягвайки комисионните на Booking.com, Expedia и TripAdvisor."
                }
                return {"text": responses.get(lang, responses['en']), "action": "open_website"}
            
            # TRAVEL PLANNING TRIGGERS
            if any(k in text_lower for k in ['voli', 'flights', 'volo', 'aereo', 'plane', 'skyscanner', 'полет', 'самолет']):
                responses = {
                    'it': "Apro Skyscanner! Confronta i prezzi ma prenota sempre direttamente con la compagnia aerea per risparmiare il 20-25%.",
                    'en': "Opening Skyscanner! Compare prices but always book directly with the airline to save 20-25%.",
                    'bg': "Отварям Skyscanner! Сравни цените, но винаги резервирай директно при авиокомпанията, за да спестиш 20-25%."
                }
                return {"text": responses.get(lang, responses['en']), "action": "open_skyscanner"}
            
            if any(k in text_lower for k in ['treno', 'treni', 'train', 'trenitalia', 'влак']):
                responses = {
                    'it': "Apro Trenitalia! Prenota direttamente sul loro sito per le migliori tariffe.",
                    'en': "Opening Trenitalia! Book directly on their site for the best rates.",
                    'bg': "Отварям Trenitalia! Резервирай директно на техния сайт за най-добрите цени."
                }
                return {"text": responses.get(lang, responses['en']), "action": "open_trenitalia"}
            
            if any(k in text_lower for k in ['autobus', 'bus', 'etna trasporti', 'автобус']):
                responses = {
                    'it': "Apro Etna Trasporti! Il modo migliore per viaggiare in Sicilia orientale.",
                    'en': "Opening Etna Trasporti! The best way to travel around Eastern Sicily.",
                    'bg': "Отварям Etna Trasporti! Най-добрият начин да пътувате из Източна Сицилия."
                }
                return {"text": responses.get(lang, responses['en']), "action": "open_etna"}

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

REPLY IN {lang.upper()} ONLY! Be brief but complete (1-4 sentences).

EXACT FACTS:
APARTMENTS:
- BOHO: 100m², 10 guests, €500/night, bohemian, terrace with Etna view
- VINTAGE: 90m², 8 guests, €450/night, baroque, balcony over Isola Bella
- SHABBY: 90m², 8 guests, €450/night, shabby chic, pastel

LOCATION: Via Nazionale, 20m from Isola Bella
SUPERMARKET: Below Cohen House
BOOKING: **ALWAYS EMPHASIZE**: Save 20-25% by booking directly at www.cohenhouse.it instead of Booking.com, Expedia, or TripAdvisor (intermediaries charge very high commissions!)

COHEN HOUSE LANDMARKS:
- Stunning terraces with panoramic Mount Etna and sea views
- Historic Via Nazionale location - heart of Taormina
- Steps from Isola Bella nature reserve (UNESCO World Heritage)
- Walking distance to ancient Greek Theatre (Teatro Greco)
- Beautiful baroque architecture with modern luxury amenities
- Private balconies overlooking the Ionian Sea
- Original Sicilian tile work and period details
- Rooftop terrace with sunset views over Taormina Bay

TAORMINA ATTRACTIONS (Expert Knowledge):
- Teatro Greco (Greek Theatre): Ancient amphitheater with Etna backdrop, 3rd century BC
- Isola Bella: Protected nature reserve, pearl of the Ionian Sea, cable car access
- Corso Umberto: Main shopping street with boutiques and cafes
- Piazza IX Aprile: Panoramic square with stunning views
- Villa Comunale Gardens: Beautiful public gardens with exotic plants
- Castelmola: Medieval village above Taormina, famous almond wine
- Giardini Naxos: First Greek colony in Sicily, beautiful beaches
- Mazzarò Beach: Stunning bay accessible by cable car

ITALIAN & SICILY HISTORY (Expert):
- Sicily: Greek colonization 8th century BC, then Roman, Byzantine, Arab, Norman rule
- Taormina: Founded by Greeks in 358 BC, strategic position attracted many civilizations
- Mount Etna: Europe's highest active volcano (3,329m), shaped Sicilian culture
- Norman-Arab-Byzantine influence created unique Sicilian architecture
- Kingdom of Two Sicilies: Spanish and Bourbon rule until Italian unification 1860
- Rich culinary tradition: Greek, Arab, Norman, Spanish influences
- Sicilian Baroque: UNESCO World Heritage style after 1693 earthquake
- Ancient Greek temples: Valley of Temples, Segesta, Selinunte

TRAVEL PLANNING ADVICE:
- **CRITICAL**: Always book directly through merchant websites to save 20-25%
- Avoid intermediaries like Booking.com, Expedia, TripAdvisor (excessive commissions!)
- Direct booking = better prices, direct communication, more flexibility
- For Cohen House: www.cohenhouse.it (best rates guaranteed)
- Transportation: Trenitalia for trains, Etna Trasporti for local buses
- Flights: Compare on Skyscanner but book directly with airlines

NAME:
- IT: "Mi chiamo Solomon!"
- EN: "I'm Solomon!"
- BG: "Аз съм Соломон!"
"""

            response = await self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": text}
                ],
                max_tokens=200,
                temperature=0.3
            )

            return {"text": response.choices[0].message.content.strip(), "action": None}

        except Exception as e:
            return {"text": "info@cohenhouse.com", "action": None}

assistant = OpenAIAssistant()
