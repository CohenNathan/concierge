"""
Ring Authentication - Manual Token Extraction
"""
import json
from pathlib import Path

TOKEN_FILE = Path.home() / ".ring_token.json"

def create_token_manually():
    print("🌐 MANUAL RING TOKEN SETUP")
    print("=" * 70)
    print("\nSTEP 1: Open Ring website")
    print("  → Go to: https://ring.com/")
    print("  → Login with your Ring account\n")
    
    print("STEP 2: Open Browser Developer Tools")
    print("  → Press F12 (or Cmd+Option+I on Mac)")
    print("  → Go to the 'Network' tab\n")
    
    print("STEP 3: Trigger an API call")
    print("  → Refresh the page (F5)")
    print("  → Or click on 'Devices' or any menu item\n")
    
    print("STEP 4: Find the Authorization token")
    print("  → In Network tab, find any request to 'api.ring.com'")
    print("  → Click on it")
    print("  → Go to 'Headers' section")
    print("  → Find 'Authorization: Bearer ...'")
    print("  → Copy ONLY the long token after 'Bearer '\n")
    
    print("=" * 70)
    print("\nExample token looks like:")
    print("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY...")
    print("(very long string with dots)")
    print("=" * 70 + "\n")
    
    access_token = input("Paste your access_token here: ").strip()
    
    if not access_token or len(access_token) < 50:
        print("\n❌ Token too short! Please copy the full token.")
        return False
    
    token = {
        "access_token": access_token,
        "token_type": "Bearer",
        "expires_in": 3600
    }
    
    with open(TOKEN_FILE, 'w') as f:
        json.dump(token, f, indent=2)
    
    print(f"\n✅ Token saved to {TOKEN_FILE}")
    return True

if __name__ == "__main__":
    create_token_manually()
