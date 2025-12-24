from openai import AsyncOpenAI
import os
from dotenv import load_dotenv

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
            
            text = text.strip()
            if len(text) < 2:
                return {"text": "Come posso aiutarti?" if lang == "it" else "How can I help you?", "action": None}
            
            text_lower = text.lower()

            # MUSIC DETECTION - Check specific types first
            music_type_found = None
            
            # Political (check first - most specific)
            if any(k in text_lower for k in ['politica', 'political', 'marinno', 'deija']):
                music_type_found = "play_political"
            
            # Love / Romantic
            elif any(k in text_lower for k in ['amore', 'love', 'romantica', 'romantic', 'impero', 'mannarino']):
                music_type_found = "play_love"
            
            # Fun
            elif any(k in text_lower for k in ['divertente', 'fun', 'funny', 'bambole', 'allegra', 'vogliamo']):
                music_type_found = "play_fun"
            
            # Traditional
            elif any(k in text_lower for k in ['tradizionale', 'traditional', 'pizzica', 'tarantella']):
                music_type_found = "play_pizzica"
            
            # If music type found, play immediately
            if music_type_found:
                self.awaiting_music_choice = False
                return {
                    "text": MUSIC_FIRE_PHRASE,
                    "action": music_type_found
                }
            
            # Generic music request - ask what type
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

            # Reset awaiting state if we were waiting for music choice
            if self.awaiting_music_choice:
                self.awaiting_music_choice = False

            # Language-specific system prompts - SIMPLIFIED & CLEAR
            if lang == 'it':
                system = """Sei Solomon, il concierge magico di Cohen House Taormina.
Rispondi SOLO in ITALIANO. MAI in inglese. Massimo 2-3 frasi.

APPARTAMENTI:
- BOHO: 100m², 10 persone, €500/notte, terrazza vista Etna e mare
- VINTAGE: 90m², 8 persone, €450/notte, barocco siciliano, balcone Isola Bella
- SHABBY: 90m², 8 persone, €450/notte, shabby chic romantico

POSIZIONE: Via Nazionale, Taormina - 20 metri da Isola Bella (30 secondi a piedi)
SUPERMERCATO: Piano terra Cohen House + di fronte Isola Bella
SPIAGGIA: Isola Bella 20m, Mazzarò 5 minuti a piedi

TRASPORTI:
- Bus Catania: dopo Hotel Panoramic, €5-7, 70min (ogni 60-90min)
- Bus Messina: ingresso Isola Bella, €4-6, 50min
- Stazione treni: Taormina-Giardini 3km, taxi €15-20
- Aeroporto Catania: 50km, transfer privato €80, taxi €70, bus €8

PRENOTAZIONE DIRETTA: Risparmia 20-25% su www.cohenhouse.it
CONTATTO: info@cohenhouse.com | WhatsApp +39 347 887 9992

Il tuo nome: Mi chiamo Solomon!
NON DIRE MAI: "How can I assist" o "How may I help" - parla solo italiano!"""
            else:  # English
                system = """You are Solomon, the magical bear concierge at Cohen House Taormina.
Reply ONLY in ENGLISH. NEVER in Italian. Maximum 2-3 sentences.

APARTMENTS:
- BOHO: 100m², 10 guests, €500/night, terrace with Etna & sea view
- VINTAGE: 90m², 8 guests, €450/night, Sicilian baroque, Isola Bella balcony
- SHABBY: 90m², 8 guests, €450/night, romantic shabby chic

LOCATION: Via Nazionale, Taormina - 20 meters from Isola Bella (30 seconds walk)
SUPERMARKET: Ground floor Cohen House + opposite Isola Bella
BEACH: Isola Bella 20m, Mazzarò 5 minutes walk

TRANSPORT:
- Bus to Catania: after Hotel Panoramic, €5-7, 70min (every 60-90min)
- Bus to Messina: Isola Bella entrance, €4-6, 50min
- Train station: Taormina-Giardini 3km, taxi €15-20
- Catania airport: 50km, private transfer €80, taxi €70, bus €8

DIRECT BOOKING: Save 20-25% at www.cohenhouse.it
CONTACT: info@cohenhouse.com | WhatsApp +39 347 887 9992

Your name: I'm Solomon!
NEVER SAY: "How can I assist" or "How may I help" - speak only English!"""

            # Call OpenAI with simplified system prompt
            response = await self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": text}
                ],
                max_tokens=100,  # Shorter for faster responses
                temperature=0.7
            )
            
            response_text = response.choices[0].message.content.strip()
            
            # Simple language validation - if wrong language, use fallback
            if lang == "it":
                english_words = ['how', 'may', 'assist', 'help', 'welcome', 'hello', 'please']
                if sum(1 for w in english_words if w in response_text.lower()) >= 2:
                    print("⚠️ AI used English, using Italian fallback")
                    return {"text": "Ciao! Come posso aiutarti?", "action": None}
            elif lang == "en":
                italian_words = ['ciao', 'buongiorno', 'come', 'posso', 'aiutarti']
                if sum(1 for w in italian_words if w in response_text.lower()) >= 2:
                    print("⚠️ AI used Italian, using English fallback")
                    return {"text": "Hello! How can I help you?", "action": None}
            
            return {"text": response_text, "action": None}

        except Exception as e:
            print(f"❌ Assistant error: {e}")
            return {"text": "info@cohenhouse.com", "action": None}

assistant = OpenAIAssistant()
