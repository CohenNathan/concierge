import json
from ring_doorbell import Auth, Ring
from pathlib import Path

TOKEN_FILE = Path.home() / ".ring_token.json"

def setup_ring():
    """Setup Ring with 2FA support"""
    print("🔐 Ring Doorbell Authentication")
    print("=" * 50)
    
    username = input("Enter Ring email: ").strip()
    password = input("Enter Ring password: ").strip()
    
    auth = Auth("CohenHouseAI/1.0", None, token_updater=lambda token: save_token(token))
    
    try:
        auth.fetch_token(username, password)
        print("\n✅ Authentication successful!")
        
    except Exception as e:
        if "2fa" in str(e).lower():
            print("\n📱 2FA Required!")
            code = input("Enter 2FA code from email/SMS: ").strip()
            
            try:
                auth.fetch_token(username, password, code)
                print("\n✅ Authentication successful with 2FA!")
            except Exception as e2:
                print(f"\n❌ 2FA failed: {e2}")
                return False
        else:
            print(f"\n❌ Authentication failed: {e}")
            return False
    
    # Save token
    save_token(auth.token)
    
    # Test the connection
    ring = Ring(auth)
    devices = ring.devices()
    
    print(f"\n🎉 Found {len(devices['doorbots'])} doorbell(s)")
    for doorbell in devices['doorbots']:
        print(f"   📹 {doorbell['description']}")
    
    return True

def save_token(token):
    """Save token to file"""
    with open(TOKEN_FILE, 'w') as f:
        json.dump(token, f)
    print(f"💾 Token saved to {TOKEN_FILE}")

if __name__ == "__main__":
    setup_ring()
