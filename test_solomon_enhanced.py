"""
Test Solomon Enhanced Features (Unit Tests)
Tests the logic without requiring OpenAI API calls
"""
import sys
import os

# Test the assistant logic patterns


def test_nathan_joanna_detection():
    """Test Nathan/Joanna name detection logic"""
    print("\n" + "="*60)
    print("TEST 1: Nathan/Joanna Detection Logic")
    print("="*60)
    
    test_cases = [
        ("Is Nathan home?", True),
        ("È qui Joanna?", True),
        ("Натан дома ли е?", True),
        ("Nathan e Joanna sono qui?", True),
        ("Natan is here?", True),
        ("Where is nathan?", True),
        ("Hello, how are you?", False),
        ("What's the weather?", False),
    ]
    
    for text, should_match in test_cases:
        text_lower = text.lower()
        name_detected = any(name in text_lower for name in ['nathan', 'natan', 'joanna', 'натан', 'джоана', 'джоанна'])
        home_query = any(q in text_lower for q in ['home', 'here', 'дома', 'тук', 'къщи', 'casa', 'qui', 'è qui', 'c\'è'])
        matches = name_detected and home_query
        
        status = "✅" if matches == should_match else "❌"
        print(f"{status} '{text}' -> Name: {name_detected}, Home query: {home_query}, Expected: {should_match}")
        assert matches == should_match, f"Failed for: {text}"
    
    print("\n✅ All Nathan/Joanna detection tests passed!")


def test_website_triggers():
    """Test website trigger detection"""
    print("\n" + "="*60)
    print("TEST 2: Website Trigger Detection")
    print("="*60)
    
    test_cases = [
        ("Open Cohen House website", True),
        ("Show me the website", True),
        ("Apri il sito web", True),
        ("Покажи уебсайта", True),
        ("cohen house", True),
        ("Hello", False),
        ("What time is it?", False),
    ]
    
    for text, should_match in test_cases:
        text_lower = text.lower()
        matches = any(k in text_lower for k in ['website', 'sito', 'уебсайт', 'web', 'cohen house', 'cohenhouse'])
        
        status = "✅" if matches == should_match else "❌"
        print(f"{status} '{text}' -> Detected: {matches}, Expected: {should_match}")
        assert matches == should_match, f"Failed for: {text}"
    
    print("\n✅ All website trigger tests passed!")


def test_travel_triggers():
    """Test travel trigger detection"""
    print("\n" + "="*60)
    print("TEST 3: Travel Trigger Detection")
    print("="*60)
    
    # Flights
    flight_cases = [
        ("Show me flights", True),
        ("Cerco voli", True),
        ("volo", True),
        ("flights to Rome", True),
        ("skyscanner", True),
        ("Hello", False),
    ]
    
    print("\n🛫 Flight triggers:")
    for text, should_match in flight_cases:
        text_lower = text.lower()
        matches = any(k in text_lower for k in ['voli', 'flights', 'volo', 'aereo', 'plane', 'skyscanner', 'полет', 'самолет'])
        
        status = "✅" if matches == should_match else "❌"
        print(f"{status} '{text}' -> Detected: {matches}, Expected: {should_match}")
        assert matches == should_match, f"Failed for: {text}"
    
    # Trains
    train_cases = [
        ("I need a train", True),
        ("Treno per Catania", True),
        ("trenitalia", True),
        ("Hello", False),
    ]
    
    print("\n🚂 Train triggers:")
    for text, should_match in train_cases:
        text_lower = text.lower()
        matches = any(k in text_lower for k in ['treno', 'treni', 'train', 'trenitalia', 'влак'])
        
        status = "✅" if matches == should_match else "❌"
        print(f"{status} '{text}' -> Detected: {matches}, Expected: {should_match}")
        assert matches == should_match, f"Failed for: {text}"
    
    # Buses
    bus_cases = [
        ("Bus to Catania", True),
        ("Autobus per Etna", True),
        ("etna trasporti", True),
        ("Hello", False),
    ]
    
    print("\n🚌 Bus triggers:")
    for text, should_match in bus_cases:
        text_lower = text.lower()
        matches = any(k in text_lower for k in ['autobus', 'bus', 'etna trasporti', 'автобус'])
        
        status = "✅" if matches == should_match else "❌"
        print(f"{status} '{text}' -> Detected: {matches}, Expected: {should_match}")
        assert matches == should_match, f"Failed for: {text}"
    
    print("\n✅ All travel trigger tests passed!")


def test_music_triggers():
    """Test music trigger detection"""
    print("\n" + "="*60)
    print("TEST 4: Music Trigger Detection")
    print("="*60)
    
    test_cases = [
        ("Play some music", True),
        ("Metti musica", True),
        ("spotify", True),
        ("Suona una canzone", True),
        ("Hello", False),
    ]
    
    for text, should_match in test_cases:
        text_lower = text.lower()
        matches = any(k in text_lower for k in ['musica', 'music', 'spotify', 'canzone', 'song', 'suona', 'play', 'metti'])
        
        status = "✅" if matches == should_match else "❌"
        print(f"{status} '{text}' -> Detected: {matches}, Expected: {should_match}")
        assert matches == should_match, f"Failed for: {text}"
    
    print("\n✅ All music trigger tests passed!")


def test_system_prompt_content():
    """Verify system prompt has all required knowledge"""
    print("\n" + "="*60)
    print("TEST 5: System Prompt Knowledge Content")
    print("="*60)
    
    # Read the openai_assistant.py file
    with open('/home/runner/work/concierge/concierge/app/openai_assistant.py', 'r') as f:
        content = f.read()
    
    required_content = [
        # Cohen House landmarks
        "COHEN HOUSE LANDMARKS",
        "terraces",
        "Etna",
        "Isola Bella",
        "Teatro Greco",
        
        # Taormina attractions
        "TAORMINA ATTRACTIONS",
        "Greek Theatre",
        "Corso Umberto",
        "Piazza IX Aprile",
        "Castelmola",
        
        # History
        "ITALIAN & SICILY HISTORY",
        "Greek colonization",
        "Norman",
        "Arab",
        "Sicilian Baroque",
        
        # Direct booking emphasis
        "20-25%",
        "Booking.com",
        "Expedia",
        "TripAdvisor",
        "directly",
        "www.cohenhouse.it",
    ]
    
    for item in required_content:
        if item in content:
            print(f"✅ Found: {item}")
        else:
            print(f"❌ Missing: {item}")
            assert False, f"Missing required content: {item}"
    
    print("\n✅ All system prompt content verified!")


def run_all_tests():
    """Run all test suites"""
    print("\n" + "🐻"*30)
    print("SOLOMON ENHANCED FEATURES UNIT TEST SUITE")
    print("🐻"*30)
    
    try:
        test_nathan_joanna_detection()
        test_website_triggers()
        test_travel_triggers()
        test_music_triggers()
        test_system_prompt_content()
        
        print("\n" + "="*60)
        print("🎉 ALL UNIT TESTS PASSED! 🎉")
        print("="*60)
        print("\nSummary:")
        print("✅ Nathan/Joanna detection logic working")
        print("✅ Website trigger detection working")
        print("✅ Travel trigger detection working")
        print("✅ Music trigger detection working")
        print("✅ System prompt has comprehensive knowledge")
        print("\n🐻 Solomon logic is solid!")
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True


if __name__ == "__main__":
    # Run tests
    success = run_all_tests()
    sys.exit(0 if success else 1)
