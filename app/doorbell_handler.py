"""
Ultra-Luxury Human Concierge for Cohen House
"""
import asyncio
import subprocess
from pathlib import Path
import random
from datetime import datetime

class DoorbellHandler:
    def __init__(self):
        self.tts = None
        self.base_dir = Path(__file__).parent.parent
        
        self.concierge_names = {
            'it': 'Alessandro',
            'en': 'James',
            'bg': 'Николай',
        }
    
    def get_time_greeting(self, language='it'):
        hour = datetime.now().hour
        
        greetings = {
            'it': {
                'morning': 'Buongiorno',
                'afternoon': 'Buon pomeriggio',
                'evening': 'Buonasera'
            },
            'en': {
                'morning': 'Good morning',
                'afternoon': 'Good afternoon',
                'evening': 'Good evening'
            },
            'bg': {
                'morning': 'Добро утро',
                'afternoon': 'Добър ден',
                'evening': 'Добър вечер'
            }
        }
        
        if 6 <= hour < 12:
            period = 'morning'
        elif 12 <= hour < 18:
            period = 'afternoon'
        else:
            period = 'evening'
        
        return greetings.get(language, greetings['it'])[period]
    
    async def ultra_luxury_greeting(self, language='it'):
        """Human concierge greeting"""
        time_greeting = self.get_time_greeting(language)
        name = self.concierge_names.get(language, 'Alessandro')
        
        greetings = {
            'it': [
                f"{time_greeting}, benvenuti a Cohen House. Sono {name}, il portiere capo.",
            ],
            'en': [
                f"{time_greeting}, welcome to Cohen House. I'm {name}, the head concierge.",
            ],
            'bg': [
                f"{time_greeting}, добре дошли в Cohen House. Аз съм {name}, главен портиер.",
            ]
        }
        
        greeting_variants = greetings.get(language, greetings['it'])
        text = random.choice(greeting_variants)
        
        print(f"🎩 Greeting: '{text}' ({language})")
        
        if self.tts:
            try:
                audio_data = await self.tts.generate(text, language)
                audio_path = self.base_dir / audio_data['audio_url'].replace('/tts/', 'data/tts/')
                subprocess.run(['afplay', str(audio_path)], check=True)
                print(f"✅ Played greeting")
            except Exception as e:
                print(f"❌ Greeting error: {e}")
        
        return True
    
    async def handle_ring_event(self, event):
        """Handle doorbell"""
        event_type = event.get('kind')
        
        if event_type == 'ding':
            print(f"🔔 DOORBELL - VIP Protocol")
            await self.ultra_luxury_greeting('it')
            return True
        
        return False
