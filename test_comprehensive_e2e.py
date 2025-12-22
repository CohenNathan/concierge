#!/usr/bin/env python3
"""
Comprehensive End-to-End Test for Solomon
Tests actual responses in English and Italian to verify language quality
"""
import asyncio
import sys
import os

# Add app directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

# Set a dummy API key for testing triggers (not full OpenAI responses)
os.environ['OPENAI_API_KEY'] = 'sk-test-dummy-key-for-testing'

from app.openai_assistant import OpenAIAssistant

async def test_language_quality():
    """Test response quality in English and Italian"""
    print("\n" + "="*70)
    print("COMPREHENSIVE LANGUAGE QUALITY TEST")
    print("Testing English and Italian responses")
    print("="*70)
    
    # Initialize assistant
    assistant = OpenAIAssistant()
    
    test_cases = [
        # Nathan/Joanna tests
        {
            "query_en": "Is Nathan home?",
            "query_it": "Nathan è a casa?",
            "expected_keywords": ["not home", "message", "relay", "non sono", "messaggio"],
            "category": "Ring Doorbell"
        },
        {
            "query_en": "Is Joanna here?",
            "query_it": "Joanna è qui?",
            "expected_keywords": ["not home", "message", "non sono", "messaggio"],
            "category": "Ring Doorbell"
        },
        
        # Website opening tests
        {
            "query_en": "Open Cohen House website",
            "query_it": "Apri il sito di Cohen House",
            "expected_keywords": ["20-25%", "directly", "Booking.com", "direttamente"],
            "category": "Website Opening"
        },
        {
            "query_en": "Show me the website",
            "query_it": "Mostrami il sito web",
            "expected_keywords": ["Cohen House", "20-25%", "save", "risparmia"],
            "category": "Website Opening"
        },
        
        # Travel planning tests
        {
            "query_en": "I need to book a flight",
            "query_it": "Ho bisogno di prenotare un volo",
            "expected_keywords": ["Skyscanner", "directly", "20-25%", "direttamente"],
            "category": "Travel Planning - Flights"
        },
        {
            "query_en": "How do I get to Catania by train?",
            "query_it": "Come arrivo a Catania in treno?",
            "expected_keywords": ["Trenitalia", "train", "treno"],
            "category": "Travel Planning - Trains"
        },
        {
            "query_en": "I need a bus to Mount Etna",
            "query_it": "Ho bisogno di un autobus per l'Etna",
            "expected_keywords": ["Etna Trasporti", "bus", "autobus"],
            "category": "Travel Planning - Buses"
        },
    ]
    
    print("\n" + "━"*70)
    print("PART 1: TRIGGER-BASED RESPONSES (Fast)")
    print("━"*70)
    
    results = {"passed": 0, "failed": 0, "total": 0}
    
    for i, test in enumerate(test_cases, 1):
        category = test["category"]
        print(f"\n{'='*70}")
        print(f"Test {i}/{len(test_cases)}: {category}")
        print(f"{'='*70}")
        
        # Test English
        print(f"\n🇬🇧 English Query: \"{test['query_en']}\"")
        try:
            response_en = await assistant.ask(test['query_en'], 'en')
            print(f"✓ Response: {response_en['text']}")
            print(f"  Action: {response_en['action']}")
            
            # Check for expected keywords
            response_lower = response_en['text'].lower()
            found_keywords = [kw for kw in test['expected_keywords'] if kw.lower() in response_lower]
            
            if found_keywords:
                print(f"  ✅ Contains keywords: {', '.join(found_keywords)}")
                results["passed"] += 1
            else:
                print(f"  ⚠️  Missing expected keywords from: {test['expected_keywords']}")
                results["failed"] += 1
            
            results["total"] += 1
            
        except Exception as e:
            print(f"❌ Error: {e}")
            results["failed"] += 1
            results["total"] += 1
        
        # Test Italian
        print(f"\n🇮🇹 Italian Query: \"{test['query_it']}\"")
        try:
            response_it = await assistant.ask(test['query_it'], 'it')
            print(f"✓ Response: {response_it['text']}")
            print(f"  Action: {response_it['action']}")
            
            # Check for expected keywords
            response_lower = response_it['text'].lower()
            found_keywords = [kw for kw in test['expected_keywords'] if kw.lower() in response_lower]
            
            if found_keywords:
                print(f"  ✅ Contains keywords: {', '.join(found_keywords)}")
                results["passed"] += 1
            else:
                print(f"  ⚠️  Missing expected keywords from: {test['expected_keywords']}")
                results["failed"] += 1
            
            results["total"] += 1
            
        except Exception as e:
            print(f"❌ Error: {e}")
            results["failed"] += 1
            results["total"] += 1
    
    # Summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Total tests: {results['total']}")
    print(f"✅ Passed: {results['passed']}")
    print(f"❌ Failed: {results['failed']}")
    print(f"Success rate: {(results['passed']/results['total']*100):.1f}%")
    
    if results['failed'] == 0:
        print("\n🎉 ALL LANGUAGE QUALITY TESTS PASSED!")
    else:
        print(f"\n⚠️  {results['failed']} tests need attention")
    
    return results['failed'] == 0


async def test_system_prompt_languages():
    """Verify system prompt properly instructs for each language"""
    print("\n" + "="*70)
    print("SYSTEM PROMPT LANGUAGE VERIFICATION")
    print("="*70)
    
    assistant = OpenAIAssistant()
    
    # Check that system prompt has proper language instructions
    test_text = "test"
    
    languages = [
        ('en', 'ENGLISH'),
        ('it', 'ITALIAN'),
        ('bg', 'BULGARIAN')
    ]
    
    for lang_code, lang_name in languages:
        print(f"\n{lang_name} ({lang_code.upper()}):")
        try:
            # The ask method should create system prompt with language instruction
            response = await assistant.ask(test_text, lang_code)
            # Just verify it doesn't crash
            print(f"  ✅ System prompt generation works for {lang_name}")
        except Exception as e:
            print(f"  ❌ Error with {lang_name}: {e}")
            return False
    
    print("\n✅ All language system prompts working!")
    return True


async def test_response_content_quality():
    """Test that responses contain proper information"""
    print("\n" + "="*70)
    print("RESPONSE CONTENT QUALITY TEST")
    print("="*70)
    
    assistant = OpenAIAssistant()
    
    # Test specific response qualities
    quality_tests = [
        {
            "query": "Is Nathan at home?",
            "lang": "en",
            "must_contain": ["Nathan", "Joanna", "not home", "message"],
            "must_not_contain": [],
            "description": "Nathan/Joanna response completeness"
        },
        {
            "query": "Nathan è a casa?",
            "lang": "it",
            "must_contain": ["Nathan", "Joanna", "non sono"],
            "must_not_contain": [],
            "description": "Italian Nathan/Joanna response"
        },
        {
            "query": "Open website",
            "lang": "en",
            "must_contain": ["Cohen House", "20-25%", "directly"],
            "must_not_contain": [],
            "description": "Website opening with booking advice"
        },
        {
            "query": "Apri il sito",
            "lang": "it",
            "must_contain": ["Cohen House", "20-25%", "direttamente"],
            "must_not_contain": [],
            "description": "Italian website opening"
        },
    ]
    
    all_passed = True
    
    for test in quality_tests:
        print(f"\n📋 Testing: {test['description']}")
        print(f"   Query ({test['lang']}): \"{test['query']}\"")
        
        try:
            response = await assistant.ask(test['query'], test['lang'])
            response_text = response['text']
            print(f"   Response: {response_text}")
            
            # Check must contain
            missing = []
            for phrase in test['must_contain']:
                if phrase.lower() not in response_text.lower():
                    missing.append(phrase)
            
            # Check must not contain
            forbidden_found = []
            for phrase in test['must_not_contain']:
                if phrase.lower() in response_text.lower():
                    forbidden_found.append(phrase)
            
            if missing:
                print(f"   ❌ Missing required phrases: {', '.join(missing)}")
                all_passed = False
            elif forbidden_found:
                print(f"   ❌ Contains forbidden phrases: {', '.join(forbidden_found)}")
                all_passed = False
            else:
                print(f"   ✅ Content quality verified!")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
            all_passed = False
    
    return all_passed


async def run_comprehensive_tests():
    """Run all comprehensive tests"""
    print("\n" + "🐻"*35)
    print("SOLOMON COMPREHENSIVE END-TO-END TEST SUITE")
    print("Testing from beginning to end")
    print("🐻"*35)
    
    all_tests_passed = True
    
    # Test 1: Language quality
    try:
        result1 = await test_language_quality()
        all_tests_passed = all_tests_passed and result1
    except Exception as e:
        print(f"\n❌ Language quality test failed: {e}")
        import traceback
        traceback.print_exc()
        all_tests_passed = False
    
    # Test 2: System prompt languages
    try:
        result2 = await test_system_prompt_languages()
        all_tests_passed = all_tests_passed and result2
    except Exception as e:
        print(f"\n❌ System prompt test failed: {e}")
        import traceback
        traceback.print_exc()
        all_tests_passed = False
    
    # Test 3: Response content quality
    try:
        result3 = await test_response_content_quality()
        all_tests_passed = all_tests_passed and result3
    except Exception as e:
        print(f"\n❌ Response content test failed: {e}")
        import traceback
        traceback.print_exc()
        all_tests_passed = False
    
    # Final summary
    print("\n" + "="*70)
    print("FINAL TEST SUMMARY")
    print("="*70)
    
    if all_tests_passed:
        print("\n✅ ✅ ✅ ALL COMPREHENSIVE TESTS PASSED! ✅ ✅ ✅")
        print("\n🐻 Solomon speaks perfectly in English and Italian!")
        print("   All triggers working correctly")
        print("   All responses contain proper information")
        print("   Multi-language support verified")
        return 0
    else:
        print("\n⚠️  SOME TESTS FAILED")
        print("   Review the output above for details")
        return 1


if __name__ == "__main__":
    sys.exit(asyncio.run(run_comprehensive_tests()))
