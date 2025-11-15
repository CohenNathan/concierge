import asyncio
import json
from pathlib import Path
from ring_doorbell import Ring, Auth
import warnings
warnings.filterwarnings('ignore')

async def check():
    with open(Path.home() / ".ring_token.json") as f:
        token = json.load(f)
    
    auth = Auth("Test/1.0", token, lambda t: None)
    ring = Ring(auth)
    
    await ring.async_update_data()
    
    print("Ring object attributes:")
    print([attr for attr in dir(ring) if not attr.startswith('_')])
    
    print("\n\nTrying devices()...")
    try:
        devs = ring.devices()
        print(f"Type: {type(devs)}")
        print(f"Content: {devs}")
    except Exception as e:
        print(f"Error: {e}")
    
    await ring.async_close()

loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(check())
finally:
    loop.close()
