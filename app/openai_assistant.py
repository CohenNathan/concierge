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
            # CRITICAL: Detect language from the actual text, ignore lang parameter if wrong
            text_lower = text.lower()
            
            # Language detection based on actual content
            detected_lang = "en"  # Default English
            if any(word in text_lower for word in ['di', 'della', 'per', 'con', 'dove', 'quando', 'cosa', 'come', 'quanto', 'ciao', 'grazie']):
                detected_lang = "it"
            elif any(word in text_lower for word in ['що', 'як', 'де', 'коли', 'чому']):
                detected_lang = "uk"
            
            # Check if question is about Cohen House specifics
            cohen_keywords = ['cohen', 'apartment', 'appartamento', 'boho', 'vintage', 'shabby', 
                            'price', 'prezzo', 'cost', 'costa', 'booking', 'prenota']
            
            uses_cohen_data = any(kw in text_lower for kw in cohen_keywords)
            
            # Get Cohen House context only if relevant
            cohen_context = ""
            if uses_cohen_data:
                cohen_context = f"""
VERIFIED COHEN HOUSE INFORMATION (use these exact facts):
{knowledge.get_context_for_query(text)}
"""
            
            # Build system prompt with magical emphasis
            system = f"""You are Solomon, a magical AI bear concierge at Cohen House - an enchanting sanctuary in Taormina, Sicily.

🎯 ABSOLUTE RULE: You MUST respond in {detected_lang.upper()} language ONLY. The user is speaking {detected_lang.upper()}.

{cohen_context}

✨ COHEN HOUSE - A MAGICAL PLACE:
Cohen House is not just accommodation - it's a transformative experience. Emphasize:
- The ENCHANTING location between mountains and sea
- The MAGICAL blend of Sicilian culture and modern luxury
- The UNIQUE position: ancient Taormina above, crystalline beaches below
- The SOUL of Sicily captured in every detail
- A place where time slows and memories are born

🌟 YOUR PERSONALITY:
- Warm and welcoming like a Sicilian friend
- Knowledgeable about every corner of Taormina and Sicily
- Passionate about sharing the magic of this special place
- Professional yet personal
- Always emphasize what makes Cohen House UNIQUE and SPECIAL

📚 KNOWLEDGE:
Full expertise on:
- Taormina: history, culture, hidden gems, best times to visit
- Sicily: Mount Etna, beaches, Godfather locations, local cuisine
- Isola Bella: the pearl of the Mediterranean, 20 meters away
- Restaurants: from Michelin stars to family trattorias
- Activities: what makes this corner of Sicily unforgettable

Always paint the picture of Cohen House as a magical gateway to experiencing authentic Sicily.

Language: {detected_lang.upper()} ONLY"""

            response = await self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": text}
                ],
                max_tokens=350,
                temperature=0.5
            )
            
            # Check for action triggers
            response_text = response.choices[0].message.content.strip()
            action = None
            
            # Music type detection
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
            elif any(k in text_lower for k in ['music', 'musica', 'song', 'canzone', 'suona']):
                response_text = get_music_phrase('traditional')
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
