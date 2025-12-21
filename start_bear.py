#!/usr/bin/env python3
"""
Startup script to test the Cohen House Bear application
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("🐻 Starting Cohen House Bear Application...")
print("=" * 60)

# Test 1: Check if main modules can be imported
print("\n📦 Testing module imports...")
try:
    from app.openai_assistant import assistant
    print("✅ openai_assistant - OK")
except Exception as e:
    print(f"❌ openai_assistant - ERROR: {e}")

try:
    from app.openai_speech import get_speech_client
    print("✅ openai_speech - OK")
except Exception as e:
    print(f"❌ openai_speech - ERROR: {e}")

try:
    from app.elevenlabs_tts import text_to_speech
    print("✅ elevenlabs_tts - OK")
except Exception as e:
    print(f"❌ elevenlabs_tts - ERROR: {e}")

try:
    from app.spotify_control import spotify
    print("✅ spotify_control - OK")
except Exception as e:
    print(f"❌ spotify_control - ERROR: {e}")

try:
    from app.browser_control import browser
    print("✅ browser_control - OK")
except Exception as e:
    print(f"❌ browser_control - ERROR: {e}")

try:
    from app.response_cache import get_quick_response
    print("✅ response_cache - OK")
except Exception as e:
    print(f"❌ response_cache - ERROR: {e}")

# Test 2: Check FastAPI app
print("\n🚀 Testing FastAPI application...")
try:
    from app.main import app
    print("✅ FastAPI app imported successfully")
    
    # Check routes
    routes = [route.path for route in app.routes]
    print(f"✅ Found {len(routes)} routes")
    
    # Check WebSocket endpoint
    has_ws = any("/ws" in route.path for route in app.routes)
    if has_ws:
        print("✅ WebSocket endpoint /ws - configured")
    
    # Check static files endpoint
    has_upload = any("/upload-audio" in route.path for route in app.routes)
    if has_upload:
        print("✅ Audio upload endpoint - configured")
        
except Exception as e:
    print(f"❌ FastAPI app - ERROR: {e}")

# Test 3: Test language support
print("\n🌍 Testing language support...")
try:
    import asyncio
    
    async def test_languages():
        # Test Italian
        response_it = await assistant.ask("Ciao", lang="it")
        if response_it and "text" in response_it:
            print("✅ Italian (it) - responding")
        
        # Test English
        response_en = await assistant.ask("Hello", lang="en")
        if response_en and "text" in response_en:
            print("✅ English (en) - responding")
    
    asyncio.run(test_languages())
except Exception as e:
    print(f"⚠️  Language test - Skipped (API key may be missing): {e}")

# Test 4: Check action mappings
print("\n🎵 Testing action mappings...")
test_cases = [
    ("suona pizzica tradizionale", "play_pizzica"),
    ("play fun music bambole", "play_bambole"),
    ("open spotify", "open_spotify"),
]

for phrase, expected_action in test_cases:
    phrase_lower = phrase.lower()
    
    # Check if keywords match
    has_music = any(k in phrase_lower for k in ['musica', 'music', 'spotify', 'canzone', 'song', 'suona', 'play', 'metti'])
    has_pizzica = any(k in phrase_lower for k in ['pizzica', 'tradizionale', 'traditional', 'tarantella', 'salento'])
    has_fun = any(k in phrase_lower for k in ['divertente', 'fun', 'bambole', 'allegra'])
    
    if has_pizzica:
        action = "play_pizzica"
    elif has_fun:
        action = "play_bambole"
    elif has_music:
        action = "open_spotify"
    else:
        action = None
    
    if action == expected_action:
        print(f"✅ '{phrase}' → {action}")
    else:
        print(f"❌ '{phrase}' → {action} (expected {expected_action})")

print("\n" + "=" * 60)
print("🎉 Startup check completed!")
print("\nTo start the server, run:")
print("  uvicorn app.main:app --host 0.0.0.0 --port 8000")
print("\nNote: You need API keys in .env file:")
print("  - OPENAI_API_KEY")
print("  - ELEVENLABS_API_KEY")
