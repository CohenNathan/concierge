# Solomon Assistant - Comprehensive Test Guide

## Latest Optimizations (Commit: b9a9b95 + noise filtering)

### Performance Improvements:
- ✅ Token limit: 100 → 80 (faster AI responses)
- ✅ Temperature: 0.7 → 0.6 (more consistent, faster)
- ✅ Minimum text length: 2 → 3 characters
- ✅ Noise word filtering (cough, ah, um, etc.)

---

## Test Instructions

### 1. Start the Server
```bash
cd ~/concierge
git pull origin copilot/fix-music-request-functionality
source venv/bin/activate
pkill -9 -f uvicorn
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 2. Open Browser
- Navigate to: http://localhost:8000
- Press `Cmd+Shift+R` to hard refresh
- Allow microphone access

---

## Critical Tests

### ITALIAN LANGUAGE TESTS (🇮🇹)

**Test 1: Basic Greeting**
- Say: "Ciao"
- Expected: Italian greeting response
- Should NOT contain: "Hello", "How", "assist"

**Test 2: Location Question**
- Say: "Dove si trova Cohen House?"
- Expected: Explains location in Italian (Via Nazionale, 20m da Isola Bella)
- Response time: < 2 seconds

**Test 3: Price Question**
- Say: "Quanto costa l'appartamento BOHO?"
- Expected: "€500/notte" in Italian response
- Response time: < 2 seconds

**Test 4: Traditional Music**
- Say: "Voglio musica tradizionale"
- Expected: "Orchestra... FIRE!" + Pizzica starts playing
- Music should load within 3 seconds

**Test 5: Political Music**
- Say: "Voglio musica politica" OR "Play political music"
- Expected: "Orchestra... FIRE!" + Deija starts playing
- Music should load within 3 seconds

**Test 6: Love Music**
- Say: "Musica romantica" OR "voglio musica d'amore"
- Expected: "Orchestra... FIRE!" + L'impero starts playing
- Music should load within 3 seconds

---

### ENGLISH LANGUAGE TESTS (🇬🇧)

**Test 7: Basic Greeting**
- Say: "Hello"
- Expected: English greeting response
- Should NOT contain: "Ciao", "buongiorno"

**Test 8: Location Question**
- Say: "Where is Cohen House?"
- Expected: Explains location in English (Via Nazionale, 20m from Isola Bella)
- Response time: < 2 seconds

**Test 9: Price Question**
- Say: "How much is the BOHO apartment?"
- Expected: "€500/night" in English response
- Response time: < 2 seconds

**Test 10: Traditional Music**
- Say: "Play traditional music"
- Expected: "Orchestra... FIRE!" + Pizzica starts playing
- Music should load within 3 seconds

**Test 11: Fun Music**
- Say: "Play fun music" OR "play bambole"
- Expected: "Orchestra... FIRE!" + Vogliamo le bambole starts playing
- Music should load within 3 seconds

---

### NOISE FILTERING TESTS (Should be IGNORED)

**Test 12: Cough**
- Say: "Cough cough"
- Expected: System should ignore (log: "⚠️ Filtered noise")
- Should NOT respond

**Test 13: Short Sounds**
- Say: "Ah"  or "Um" or "Er"
- Expected: System should ignore
- Should NOT respond

**Test 14: Empty/Short Input**
- Say: "..."  or "a"
- Expected: System should ignore (log: "⚠️ Ignoring empty/short input")
- Should NOT respond

---

### MUSIC TWO-STEP FLOW TESTS

**Test 15: Generic Music Request (Italian)**
- Say: "Voglio musica"
- Expected: "Che tipo di musica? Tradizionale, Divertente, Politica, o Amore?"
- Then say: "Tradizionale"
- Expected: Plays Pizzica

**Test 16: Generic Music Request (English)**
- Say: "Play music"
- Expected: "What kind of music? Traditional, Fun, Political, or Love?"
- Then say: "Love"
- Expected: Plays L'impero

---

## Performance Benchmarks

### Target Times:
- Language detection: < 1ms
- Speech-to-text (Whisper): ~0.5-0.8s
- AI response: ~0.8-1.2s
- TTS generation: ~0.5-0.8s
- **Total response time: 1.8-2.8s** (target: < 2.5s)

### Monitor Logs For:
- `✅ [IT:high]` or `✅ [EN:high]` = Good language detection
- `🤖 AI response (0.8s)` = Fast AI response
- `✅ Total time: 2.0s` = Good performance
- `⚠️ Filtered noise` = Noise filtering working

---

## Troubleshooting

### If Italian responses contain English:
- Check log for: `⚠️ AI used English, using Italian fallback`
- This means fallback is working correctly
- If happening frequently, system prompt needs strengthening

### If responses are too slow (> 3s):
- Check network latency
- Verify OpenAI API response time in logs
- Consider reducing max_tokens further (currently 80)

### If music doesn't play:
- Check Spotify is installed and logged in
- Verify `app/spotify_control.py` has correct URIs
- Check browser console for errors

### If language detection is wrong:
- Check log shows detected language: `✅ [IT:medium] IT:3 EN:0`
- If scores are equal (IT:0 EN:0), system defaults to Italian
- Very short phrases may not have enough indicators

---

## Expected Log Output (Successful Test)

```
INFO:     127.0.0.1:58660 - "WebSocket /ws" [accepted]
✅ WebSocket connected
INFO:     connection open
✅ [IT:high] IT:9 EN:0 | Ciao, dove si trova?
INFO:     127.0.0.1:58697 - "POST /upload-audio HTTP/1.1" 200 OK
🤖 AI response (0.95s)
🎤 Generating TTS [it]: Via Nazionale, 20 metri da Isola Bella!
📡 TTS response: 200
✅ TTS created: tts_xxxxx.mp3 (45000 bytes)
✅ Total time: 2.1s
```

Good indicators:
- ✅ Language detection confident (high score)
- ✅ AI response under 1 second
- ✅ Total time under 2.5 seconds
- ✅ Response in correct language

---

## Summary of Improvements

1. **Faster Responses**: 80 tokens, temperature 0.6
2. **Better Noise Filtering**: Ignores cough, um, ah, etc.
3. **Stricter Length Check**: Minimum 3 characters
4. **Cleaner System Prompts**: Direct instructions
5. **Music Priority**: Political → Love → Fun → Traditional
6. **Language Validation**: Automatic fallback if wrong language

All tests should complete successfully with these improvements!
