#!/usr/bin/env python3
"""
Performance Testing for Solomon AI
Tests loading time and response time
"""

import time
import sys
sys.path.insert(0, 'app')

print("╔══════════════════════════════════════════════════════════════════════╗")
print("║           SOLOMON PERFORMANCE TEST 🐻⚡                              ║")
print("║            Тест на производителност                                  ║")
print("╚══════════════════════════════════════════════════════════════════════╝")
print()

# Test 1: Loading Time (Време за зареждане)
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("📊 TEST 1: LOADING TIME / ВРЕМЕ ЗА ЗАРЕЖДАНЕ")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print()

start_time = time.time()

try:
    # Import OpenAI Assistant (this simulates loading Solomon)
    from openai_assistant import OpenAIAssistant
    
    load_time = time.time() - start_time
    
    print(f"✅ Solomon loaded successfully!")
    print(f"⏱️  Loading time: {load_time:.3f} seconds")
    print()
    
    if load_time < 0.5:
        print("🚀 EXCELLENT: Very fast loading (< 0.5s)")
    elif load_time < 1.0:
        print("✅ GOOD: Fast loading (< 1.0s)")
    elif load_time < 2.0:
        print("⚠️  ACCEPTABLE: Moderate loading (< 2.0s)")
    else:
        print("❌ SLOW: Loading takes too long (> 2.0s)")
    
except Exception as e:
    load_time = time.time() - start_time
    print(f"❌ Failed to load: {e}")
    print(f"⏱️  Time before failure: {load_time:.3f} seconds")
    sys.exit(1)

print()
print()

# Test 2: Response Time (Време за отговор)
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("📊 TEST 2: RESPONSE TIME / ВРЕМЕ ЗА ОТГОВОР")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print()

# Test queries (different types)
test_queries = [
    ("Is Nathan home?", "Nathan/Joanna detection"),
    ("Open Cohen House website", "Website trigger"),
    ("I need flights", "Travel trigger"),
    ("Play pizzica", "Music trigger"),
    ("Play seria music", "Seria music trigger"),
    ("Play romantic music", "Romantic music trigger"),
]

print("Testing trigger detection (no GPT API calls)...")
print()

assistant = OpenAIAssistant()
total_time = 0
results = []

for query, test_type in test_queries:
    start = time.time()
    
    try:
        # This tests the trigger detection logic only (instant, no API calls)
        import asyncio
        response = asyncio.run(assistant.ask(query, 'en'))
        
        response_time = time.time() - start
        total_time += response_time
        
        action = response.get('action', 'None')
        text_preview = response.get('text', '')[:50] + '...' if len(response.get('text', '')) > 50 else response.get('text', '')
        
        results.append({
            'query': query,
            'type': test_type,
            'time': response_time,
            'action': action,
            'text': text_preview
        })
        
        print(f"✅ {test_type}")
        print(f"   Query: \"{query}\"")
        print(f"   Time: {response_time:.4f}s")
        print(f"   Action: {action}")
        print(f"   Response: {text_preview}")
        print()
        
    except Exception as e:
        response_time = time.time() - start
        print(f"❌ {test_type}: {e}")
        print(f"   Time: {response_time:.4f}s")
        print()

# Summary
print()
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("📊 PERFORMANCE SUMMARY / ОБОБЩЕНИЕ")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print()

avg_response_time = total_time / len(test_queries) if test_queries else 0

print(f"🐻 Solomon Loading Time:  {load_time:.3f}s")
print(f"⚡ Trigger Detection Time: {avg_response_time:.4f}s (average)")
print(f"📊 Total Queries Tested:   {len(test_queries)}")
print()

# Performance Rating
print("Performance Rating:")
print()

if load_time < 1.0:
    print("  ✅ Loading: EXCELLENT")
elif load_time < 2.0:
    print("  ✅ Loading: GOOD")
else:
    print("  ⚠️  Loading: NEEDS IMPROVEMENT")

if avg_response_time < 0.001:
    print("  ✅ Response: INSTANT (< 1ms)")
elif avg_response_time < 0.01:
    print("  ✅ Response: VERY FAST (< 10ms)")
elif avg_response_time < 0.1:
    print("  ✅ Response: FAST (< 100ms)")
else:
    print("  ⚠️  Response: ACCEPTABLE")

print()
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print()

# Detailed breakdown
print("DETAILED BREAKDOWN:")
print()
print(f"{'Test Type':<30} {'Time (s)':<12} {'Action':<20}")
print("─" * 70)

for result in results:
    print(f"{result['type']:<30} {result['time']:<12.4f} {result['action']:<20}")

print()
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print()

# Notes
print("📝 NOTES:")
print()
print("• Loading time: Time to import and initialize Solomon")
print("• Response time: Time for trigger detection (instant, no API)")
print("• API calls: Would add ~0.5-2s for GPT responses (not tested here)")
print("• Temperature 0.3: Optimized for faster, more consistent responses")
print()

print("✅ Performance test completed!")
print()
