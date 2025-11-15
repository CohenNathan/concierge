#!/usr/bin/env python3
"""Generate Ring token and save to known location"""
import asyncio
import json
from pathlib import Path
from ring_doorbell import Auth

TOKEN_FILE = Path.home() / ".ring_token.json"

async def generate_token():
    username = "nathan.cohen@mail.com"
    password = input("Ring Password: ").strip()
    code = input("2FA Code: ").strip()
    
    def save_token(token):
        with open(TOKEN_FILE, 'w') as f:
            json.dump(token, f, indent=2)
        print(f"✅ Token saved to: {TOKEN_FILE}")
    
    auth = Auth("CohenHouseAI/1.0", None, save_token)
    
    try:
        await auth.async_fetch_token(username, password, code)
        print("✅ Token generated successfully!")
        
        # Show token location
        print(f"\n📍 Token saved at:")
        print(f"   {TOKEN_FILE}")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

# Run
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    result = loop.run_until_complete(generate_token())
finally:
    pending = asyncio.all_tasks(loop)
    for task in pending:
        task.cancel()
    loop.run_until_complete(asyncio.sleep(0.1))
    loop.close()
    
print("\n" + "="*50)
if result:
    print("✅ Ready to integrate Ring with Bear!")
else:
    print("❌ Token generation failed")
