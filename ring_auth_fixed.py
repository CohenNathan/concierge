#!/usr/bin/env python3
import asyncio
import json
from pathlib import Path
from ring_doorbell import Auth, Ring
import sys

TOKEN_FILE = Path.home() / ".ring_token.json"

def save_token(token):
    """Save token to file"""
    with open(TOKEN_FILE, 'w') as f:
        json.dump(token, f, indent=2)
    print(f"💾 Token saved to {TOKEN_FILE}")

async def authenticate():
    """Authenticate with Ring"""
    print("\n🔐 Ring Authentication")
    print("=" * 50)
    
    username = input("Email: ").strip()
    password = input("Password: ").strip()
    
    auth = Auth("CohenHouseAI/1.0", None, save_token)
    
    try:
        print("\n📡 Connecting to Ring API...")
        await auth.async_fetch_token(username, password)
        print("✅ Authenticated successfully!")
        
    except Exception as e:
        error_msg = str(e).lower()
        
        if "2fa" in error_msg or "verification" in error_msg:
            print("\n📱 2FA Required!")
            print("Check your email or SMS for the verification code.")
            code = input("\nEnter 2FA code: ").strip()
            
            try:
                await auth.async_fetch_token(username, password, code)
                print("✅ Authenticated with 2FA!")
            except Exception as e2:
                print(f"❌ 2FA failed: {e2}")
                return False
        else:
            print(f"❌ Authentication error: {e}")
            return False
    
    # Test the connection
    try:
        print("\n🔍 Testing Ring connection...")
        ring = Ring(auth)
        await ring.async_update_data()
        
        devices = ring.devices()
        doorbells = devices.get('doorbots', [])
        
        print(f"\n✅ Success! Found {len(doorbells)} doorbell(s):")
        for db in doorbells:
            print(f"   📹 {db.name}")
            print(f"      ID: {db.id}")
            print(f"      Battery: {db.battery_life}%")
        
        # Cleanup
        await ring.async_close()
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def main():
    """Main entry point"""
    try:
        result = asyncio.run(authenticate())
        sys.exit(0 if result else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️ Cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
