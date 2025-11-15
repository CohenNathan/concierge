import asyncio
import os
from ring_doorbell import Ring, Auth

class RingDoorbell:
    def __init__(self):
        self.ring = None
        self.doorbell = None
        self.token_file = os.path.expanduser("~/.ring_token.json")
    
    async def initialize(self):
        """Initialize Ring connection"""
        try:
            import json
            
            # Load token
            if not os.path.exists(self.token_file):
                print(f"❌ Token file not found: {self.token_file}")
                return False
            
            with open(self.token_file, 'r') as f:
                token = json.load(f)
            
            # Create auth
            auth = Auth("CohenHouseConcierge/1.0", token, None)
            
            # Create Ring instance
            self.ring = Ring(auth)
            
            # Update data
            await self.ring.async_update_data()
            
            # Get devices
            devices = self.ring.devices()
            
            if not devices or 'doorbots' not in devices or len(devices['doorbots']) == 0:
                print("❌ No doorbells found")
                return False
            
            self.doorbell = devices['doorbots'][0]
            return True
            
        except Exception as e:
            print(f"❌ Ring init error: {e}")
            return False
    
    async def get_last_event(self):
        """Get last doorbell event"""
        try:
            if not self.doorbell:
                return None
            
            history = await self.doorbell.async_history(limit=1, kind='ding')
            
            if history and len(history) > 0:
                return history[0]
            
            return None
            
        except Exception as e:
            print(f"❌ Get event error: {e}")
            return None
    
    async def close(self):
        """Close Ring connection"""
        if self.ring:
            await self.ring.async_close()
