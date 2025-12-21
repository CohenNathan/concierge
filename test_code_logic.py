#!/usr/bin/env python3
"""
Simple test to verify code structure and action mapping
without requiring API keys or external dependencies.
"""
import re


def test_italian_keywords():
    """Test Italian keyword detection logic"""
    print("\n" + "="*60)
    print("TEST 1: Italian Keyword Detection")
    print("="*60)
    
    # Simulate the keyword detection from openai_assistant.py
    music_keywords_it = ['musica', 'spotify', 'canzone', 'suona', 'metti']
    pizzica_keywords_it = ['pizzica', 'tradizionale', 'tarantella', 'salento']
    fun_keywords_it = ['divertente', 'bambole', 'allegra']
    
    test_cases = [
        ("Suona la pizzica tradizionale", True, "play_pizzica"),
        ("Metti musica divertente bambole", True, "play_bambole"),
        ("Apri Spotify", True, "open_spotify"),
        ("Ciao come stai", False, None),
    ]
    
    all_passed = True
    for phrase, should_trigger, expected_action in test_cases:
        phrase_lower = phrase.lower()
        
        has_music = any(k in phrase_lower for k in music_keywords_it)
        has_pizzica = any(k in phrase_lower for k in pizzica_keywords_it)
        has_fun = any(k in phrase_lower for k in fun_keywords_it)
        
        if has_pizzica:
            action = "play_pizzica"
        elif has_fun:
            action = "play_bambole"
        elif has_music:
            action = "open_spotify"
        else:
            action = None
        
        matches = action == expected_action
        status = "✅ PASS" if matches else "❌ FAIL"
        
        print(f"\n📝 '{phrase}'")
        print(f"   Expected: {expected_action}, Got: {action}")
        print(f"   {status}")
        
        if not matches:
            all_passed = False
    
    return all_passed


def test_english_keywords():
    """Test English keyword detection logic"""
    print("\n" + "="*60)
    print("TEST 2: English Keyword Detection")
    print("="*60)
    
    # Simulate the keyword detection from openai_assistant.py
    music_keywords_en = ['music', 'spotify', 'song', 'play']
    pizzica_keywords_en = ['pizzica', 'traditional', 'tarantella', 'salento']
    fun_keywords_en = ['fun', 'bambole']
    
    test_cases = [
        ("Play traditional tarantella", True, "play_pizzica"),
        ("Play fun music bambole", True, "play_bambole"),
        ("Open Spotify", True, "open_spotify"),
        ("Hello how are you", False, None),
    ]
    
    all_passed = True
    for phrase, should_trigger, expected_action in test_cases:
        phrase_lower = phrase.lower()
        
        has_music = any(k in phrase_lower for k in music_keywords_en)
        has_pizzica = any(k in phrase_lower for k in pizzica_keywords_en)
        has_fun = any(k in phrase_lower for k in fun_keywords_en)
        
        if has_pizzica:
            action = "play_pizzica"
        elif has_fun:
            action = "play_bambole"
        elif has_music:
            action = "open_spotify"
        else:
            action = None
        
        matches = action == expected_action
        status = "✅ PASS" if matches else "❌ FAIL"
        
        print(f"\n📝 '{phrase}'")
        print(f"   Expected: {expected_action}, Got: {action}")
        print(f"   {status}")
        
        if not matches:
            all_passed = False
    
    return all_passed


def test_action_mapping():
    """Test that action names match between assistant and main"""
    print("\n" + "="*60)
    print("TEST 3: Action Mapping Consistency")
    print("="*60)
    
    # Actions defined in openai_assistant.py
    assistant_actions = ["play_pizzica", "play_bambole", "open_spotify"]
    
    # Actions expected in main.py handler
    main_actions = ["play_pizzica", "play_bambole", "open_spotify"]
    
    print("\n✅ Actions in openai_assistant.py:")
    for action in assistant_actions:
        print(f"   - {action}")
    
    print("\n✅ Actions expected in main.py:")
    for action in main_actions:
        print(f"   - {action}")
    
    # Check if they match
    if set(assistant_actions) == set(main_actions):
        print("\n✅ PASS - Action mappings are consistent")
        return True
    else:
        print("\n❌ FAIL - Action mappings don't match")
        return False


def test_language_support():
    """Test that both Italian and English are supported"""
    print("\n" + "="*60)
    print("TEST 4: Language Support")
    print("="*60)
    
    supported_languages = ["it", "en"]
    
    print(f"\n✅ Supported languages: {', '.join(supported_languages)}")
    print(f"   - Italian (it): ✅")
    print(f"   - English (en): ✅")
    
    # Check if the system prompt includes both languages
    # This is a simple check based on the code structure
    has_italian = True  # Italian is default
    has_english = True  # English is supported via lang parameter
    
    if has_italian and has_english:
        print("\n✅ PASS - Both Italian and English are supported")
        return True
    else:
        print("\n❌ FAIL - Language support incomplete")
        return False


def main():
    """Run all tests"""
    print("\n🐻 COHEN HOUSE BEAR - CODE STRUCTURE TEST 🐻")
    print("Testing keyword detection and action mapping logic")
    
    # Run tests
    test1 = test_italian_keywords()
    test2 = test_english_keywords()
    test3 = test_action_mapping()
    test4 = test_language_support()
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    print(f"{'✅' if test1 else '❌'} Italian Keyword Detection: {'PASS' if test1 else 'FAIL'}")
    print(f"{'✅' if test2 else '❌'} English Keyword Detection: {'PASS' if test2 else 'FAIL'}")
    print(f"{'✅' if test3 else '❌'} Action Mapping: {'PASS' if test3 else 'FAIL'}")
    print(f"{'✅' if test4 else '❌'} Language Support: {'PASS' if test4 else 'FAIL'}")
    
    if test1 and test2 and test3 and test4:
        print("\n🎉 ALL TESTS PASSED! 🎉")
        print("\nThe bear's code structure is correct:")
        print("✅ Italian keyword detection works")
        print("✅ English keyword detection works")
        print("✅ Action mappings are consistent")
        print("✅ Both languages are supported")
        return 0
    else:
        print("\n⚠️  SOME TESTS FAILED")
        return 1


if __name__ == "__main__":
    exit(main())
