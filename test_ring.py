import asyncio
from app.ring_client import RingDoorbell

async def test():
    ring = RingDoorbell()
    
    print("🔔 Testing Ring Doorbell")
    print("=" * 50)
    print()
    
    if await ring.initialize():
        print(f"✅ Connected to: {ring.doorbell.name}")
        print(f"   Battery: {ring.doorbell.battery_life}%")
        print(f"   WiFi: {ring.doorbell.wifi_name}")
        print()
        
        print("🔍 Last event:")
        event = await ring.get_last_event()
        if event:
            print(f"   Type: {event.get('kind')}")
            print(f"   Time: {event.get('created_at')}")
        
        print()
        print("✅ Ring integration ready!")
    else:
        print("❌ Ring connection failed")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
