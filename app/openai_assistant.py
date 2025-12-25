import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from app.knowledge_retriever import knowledge
from app.music_phrases import get_music_phrase

load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAIAssistant:
    def __init__(self):
        self.client = client
    
    async def ask(self, text: str, lang: str = "it", **kwargs):
        try:
            # Get relevant knowledge based on query
            context = knowledge.get_context_for_query(text)
            
            # Build focused system prompt with relevant facts
            system = f"""You are Solomon, professional AI concierge at Cohen House, Taormina, Sicily.

RESPOND IN {lang.upper()} LANGUAGE ONLY. Be professional, accurate, and helpful.

VERIFIED INFORMATION ABOUT COHEN HOUSE:
{context}

BOOKING:
- Email: info@cohenhouse.com
- Website: www.cohenhouse.it  
- Direct booking saves 20-25% vs Airbnb

YOUR CAPABILITIES:
- Search flights on Skyscanner (say "open Skyscanner")
- Search trains on Trenitalia (say "open Trenitalia")
- Play Sicilian music via Spotify (traditional, fun, romantic, political)
- Provide detailed local information
- Help with bookings and reservations

Be warm and professional. Provide accurate information from the context above.
"""

            response = await self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": text}
                ],
                max_tokens=250,
                temperature=0.3
            )
            
            # Check for action triggers
            response_text = response.choices[0].message.content.strip()
            action = None
            
            text_lower = text.lower()
            
            # Music type detection with DRAMATIC phrases
            if any(k in text_lower for k in ['fun', 'party', 'bambole', 'allegr', 'festiv']):
                response_text = get_music_phrase('fun')
                action = "play_fun_music"
            elif any(k in text_lower for k in ['love', 'romantic', 'amore', 'romantico']):
                response_text = get_music_phrase('romantic')
                action = "play_love"
            elif any(k in text_lower for k in ['political', 'cultur', 'politico', 'deija']):
                response_text = get_music_phrase('political')
                action = "play_political"
            elif any(k in text_lower for k in ['traditional', 'pizzica', 'folk', 'tradizional']):
                response_text = get_music_phrase('traditional')
                action = "play_traditional"
            elif any(k in text_lower for k in ['music', 'musica', 'song', 'canzone', 'play', 'suona']):
                response_text = get_music_phrase('traditional')  # Default
                action = "play_pizzica"
            elif any(k in text_lower for k in ['flight', 'volo', 'aereo', 'skyscanner']):
                action = "open_skyscanner"
            elif any(k in text_lower for k in ['train', 'treno', 'trenitalia']):
                action = "open_trenitalia"
            
            return {"text": response_text, "action": action}
            
        except Exception as e:
            print(f"❌ AI Error: {e}")
            return {"text": "info@cohenhouse.com", "action": None}

assistant = OpenAIAssistant()
