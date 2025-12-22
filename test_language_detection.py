#!/usr/bin/env python3
"""
Test script for language detection and performance
Run this to diagnose issues with Solomon's language detection
"""

import re
import time

# Import the actual indicators from the code
ITALIAN_INDICATORS = [
    'ciao', 'buongiorno', 'buonasera', 'salve', 'buonanotte',
    'dove', 'quanto', 'costa', 'come', 'che', 'cosa', 'quando', 'perché', 'chi',
    'sei', 'sono', 'hai', 'ho', 'vuoi', 'voglio', 'posso', 'puoi',
    'senti', 'sento', 'parli', 'parlo', 'parla', 'parlare', 'capisco', 'capisci',
    'vai', 'vado', 'vieni', 'vengo', 'fa', 'fare', 'dici', 'dico', 'dire',
    'grazie', 'prego', 'scusa', 'mi', 'ti', 'chiamo', 'per', 'con', 'ma', 'e', 'o',
    'del', 'della', 'di', 'da', 'su', 'in', 'a',
    'appartamento', 'camera', 'spiaggia', 'mare', 'vicino', 'lontano',
    'uno', 'due', 'tre', 'quattro', 'cinque',
    'va', 'bene', 'non', 'si', 'sì', 'no', 'forse', 'anche',
    'italiano', 'italiana', 'inglese'
]

ENGLISH_INDICATORS = [
    'hello', 'hi', 'hey', 'good', 'morning', 'evening', 'night',
    'where', 'what', 'how', 'when', 'why', 'who', 'which',
    'is', 'are', 'can', 'do', 'does', 'have', 'has', 'want', 'need',
    'the', 'a', 'an', 'this', 'that', 'these', 'those',
    'apartment', 'room', 'beach', 'sea', 'near', 'far',
    'thank', 'please', 'sorry', 'yes', 'no', 'maybe',
    'you', 'your', 'speak', 'understand', 'tell', 'me', 'my',
    'english', 'italian', 'language', 'talk', 'say'
]

def detect_language(text):
    """Detect language using the same logic as openai_speech.py"""
    start_time = time.time()
    
    # Remove punctuation from words before matching
    text_words = re.findall(r'\b\w+\b', text.lower())
    
    # Count matches for each language
    italian_score = sum(1 for word in text_words if word in ITALIAN_INDICATORS)
    english_score = sum(1 for word in text_words if word in ENGLISH_INDICATORS)
    
    # Determine language with confidence
    if italian_score > english_score:
        lang = 'it'
        confidence = 'high' if italian_score >= 2 else 'medium'
    elif english_score > italian_score:
        lang = 'en'
        confidence = 'high' if english_score >= 2 else 'medium'
    else:
        # Default to Italian for Cohen House (most common)
        lang = 'it'
        confidence = 'low'
    
    elapsed = (time.time() - start_time) * 1000  # ms
    
    return lang, confidence, italian_score, english_score, elapsed, text_words

def main():
    print("=" * 80)
    print("LANGUAGE DETECTION TEST - Cohen House Concierge")
    print("=" * 80)
    print()
    
    # Test cases based on user's reported issues
    test_cases = [
        ("Ciao, mi senti.", "it", "Italian greeting"),
        ("Hello, do you speak English?", "en", "English question"),
        ("parli inglese", "it", "Italian asking about English"),
        ("L'italiano?", "it", "Italian question"),
        ("Good morning", "en", "English greeting"),
        ("Dove siete?", "it", "Italian location question"),
        ("How much is BOHO?", "en", "English price question"),
        ("Quanto costa BOHO?", "it", "Italian price question"),
        ("Tell me about the apartments", "en", "English info request"),
        ("Dimmi degli appartamenti", "it", "Italian info request"),
    ]
    
    print(f"Testing {len(test_cases)} phrases...")
    print()
    
    all_correct = True
    total_time = 0
    
    for text, expected_lang, description in test_cases:
        lang, confidence, it_score, en_score, elapsed, words = detect_language(text)
        total_time += elapsed
        
        is_correct = (lang == expected_lang)
        status = "✅ PASS" if is_correct else "❌ FAIL"
        
        if not is_correct:
            all_correct = False
        
        print(f"{status} | {description}")
        print(f"     Text: '{text}'")
        print(f"     Words: {words}")
        print(f"     Scores: IT={it_score}, EN={en_score}")
        print(f"     Detected: [{lang.upper()}:{confidence}] (expected: {expected_lang.upper()})")
        print(f"     Time: {elapsed:.2f}ms")
        print()
    
    avg_time = total_time / len(test_cases)
    
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Tests run: {len(test_cases)}")
    print(f"Passed: {sum(1 for t, e, _ in test_cases if detect_language(t)[0] == e)}")
    print(f"Failed: {sum(1 for t, e, _ in test_cases if detect_language(t)[0] != e)}")
    print(f"Average detection time: {avg_time:.2f}ms")
    print()
    
    if all_correct:
        print("✅ ALL TESTS PASSED! Language detection is working correctly.")
    else:
        print("❌ SOME TESTS FAILED! There may be issues with language detection.")
    
    print()
    print("=" * 80)
    print("NEXT STEPS:")
    print("=" * 80)
    print("1. Make sure you've pulled the latest changes:")
    print("   git pull origin copilot/upload-project-via-ssh-cli")
    print()
    print("2. Check that openai_speech.py has the regex fix:")
    print("   text_words = re.findall(r'\\b\\w+\\b', text.lower())")
    print()
    print("3. Restart the server to load the changes:")
    print("   uvicorn app.main:app --host 0.0.0.0 --port 8000")
    print()
    print("If tests pass but server still has issues, check:")
    print("- API keys are configured in .env")
    print("- Server logs for errors")
    print("- Network/API response times")
    print("=" * 80)

if __name__ == "__main__":
    main()
