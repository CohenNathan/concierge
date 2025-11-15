import asyncio
from app.ring_client import RingDoorbell

async def test():
    print("🔔 Testing Ring Doorbell")
    print("=" * 50)
    
    ring = RingDoorbell()
    
    if await ring.initialize():
        print(f"\n✅ Connected to: {ring.doorbell.name}")
        print(f"   Battery: {ring.doorbell.battery_life}%")
        print(f"   WiFi: {ring.doorbell.wifi_name}")
        
        print(f"\n🔍 Last event:")
        event = await ring.get_last_event()
        if event:
            print(f"   Type: {event.get('kind')}")
            print(f"   Time: {event.get('created_at')}")
        
        await ring.close()
        print("\n✅ Success!")
    else:
        print("\n❌ Failed")

loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(test())
finally:
    loop.close()
