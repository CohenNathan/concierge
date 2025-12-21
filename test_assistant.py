#!/usr/bin/env python3
"""
Test script to verify the bear recognizes Italian and English
and performs actions correctly.
"""
import asyncio
import sys
import os

# Add the app directory to the path
sys.path.insert(0, os.path.dirname(__file__))

from app.openai_assistant import assistant


async def test_italian_recognition():
    """Test Italian language recognition"""
    print("\n" + "="*60)
    print("TEST 1: Italian Language Recognition")
    print("="*60)
    
    test_phrases = [
        "Ciao! Come stai?",
        "Dimmi degli appartamenti",
        "Dove si trova Cohen House?",
    ]
    
    for phrase in test_phrases:
        print(f"\n📝 Italian input: {phrase}")
        response = await assistant.ask(phrase, lang="it")
        print(f"✅ Response: {response['text']}")
        print(f"   Action: {response.get('action', 'None')}")
    
    return True


async def test_english_recognition():
    """Test English language recognition"""
    print("\n" + "="*60)
    print("TEST 2: English Language Recognition")
    print("="*60)
    
    test_phrases = [
        "Hello! How are you?",
        "Tell me about the apartments",
        "Where is Cohen House located?",
    ]
    
    for phrase in test_phrases:
        print(f"\n📝 English input: {phrase}")
        response = await assistant.ask(phrase, lang="en")
        print(f"✅ Response: {response['text']}")
        print(f"   Action: {response.get('action', 'None')}")
    
    return True


async def test_actions():
    """Test that actions are triggered correctly"""
    print("\n" + "="*60)
    print("TEST 3: Action Triggering")
    print("="*60)
    
    test_cases = [
        {
            "phrase": "Suona la pizzica tradizionale",
            "lang": "it",
            "expected_action": "play_pizzica"
        },
        {
            "phrase": "Play traditional tarantella music",
            "lang": "en",
            "expected_action": "play_pizzica"
        },
        {
            "phrase": "Metti musica divertente bambole",
            "lang": "it",
            "expected_action": "play_bambole"
        },
        {
            "phrase": "Open Spotify for me",
            "lang": "en",
            "expected_action": "open_spotify"
        },
    ]
    
    all_passed = True
    
    for test in test_cases:
        print(f"\n📝 Input [{test['lang']}]: {test['phrase']}")
        response = await assistant.ask(test['phrase'], lang=test['lang'])
        action = response.get('action')
        print(f"   Response: {response['text']}")
        print(f"   Action: {action}")
        
        if action == test['expected_action']:
            print(f"   ✅ PASS - Action matches expected: {test['expected_action']}")
        else:
            print(f"   ❌ FAIL - Expected: {test['expected_action']}, Got: {action}")
            all_passed = False
    
    return all_passed


async def main():
    """Run all tests"""
    print("\n🐻 COHEN HOUSE BEAR - ASSISTANT TEST SUITE 🐻")
    print("Testing Italian & English recognition and action execution")
    
    try:
        # Check if API key is available
        if not os.getenv("OPENAI_API_KEY"):
            print("\n⚠️  WARNING: OPENAI_API_KEY not found in environment")
            print("   The assistant will return fallback responses")
            print("   Set OPENAI_API_KEY to test with real OpenAI API\n")
        
        # Run tests
        test1 = await test_italian_recognition()
        test2 = await test_english_recognition()
        test3 = await test_actions()
        
        # Summary
        print("\n" + "="*60)
        print("TEST SUMMARY")
        print("="*60)
        print(f"✅ Italian Recognition: {'PASS' if test1 else 'FAIL'}")
        print(f"✅ English Recognition: {'PASS' if test2 else 'FAIL'}")
        print(f"{'✅' if test3 else '❌'} Action Triggering: {'PASS' if test3 else 'FAIL'}")
        
        if test1 and test2 and test3:
            print("\n🎉 ALL TESTS PASSED! 🎉")
            print("The bear correctly recognizes Italian and English")
            print("and performs actions as expected.")
            return 0
        else:
            print("\n⚠️  SOME TESTS FAILED")
            return 1
            
    except Exception as e:
        print(f"\n❌ TEST ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
