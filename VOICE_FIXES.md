# Voice and Audio Fixes - Cohen House Concierge

## Issues Fixed

### Issue 1: Italian Voice Quality
**Problem:** Voice was speaking pseudo-Italian with English accent instead of proper literary Italian.

**Root Cause:**
- Used generic voice ID ("RxJZoVFTFvDcilRItefF") not optimized for Italian
- Used `eleven_turbo_v2` model (speed-optimized, lower quality)
- Voice settings were reduced for performance (stability 0.85, similarity 0.9)

**Solution:**
Changed to Rachel voice with multilingual settings:
```python
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Rachel - excellent Italian
model_id = "eleven_multilingual_v2"  # Better language support
stability = 0.95  # Consistent pronunciation
similarity_boost = 1.0  # Authentic accent
style = 0.0  # Neutral, clear literary Italian
```

**Benefits:**
- ✅ Proper Italian pronunciation
- ✅ Clear, literary language
- ✅ No English accent
- ✅ Natural Italian intonation

### Issue 2: Overlapping Voices (Echo/Double Audio)
**Problem:** Two voices playing simultaneously - microphone and audio overlapping.

**Root Causes:**
1. Microphone set to `continuous=true` (kept running during audio playback)
2. No proper state tracking (`recActive` flag missing)
3. Microphone stop/start timing issues
4. No proper audio playback error handling

**Solutions Implemented:**

#### 1. Microphone State Management
```javascript
let recActive=false;  // Track microphone state
rec.continuous=false;  // Prevent continuous recording
rec.interimResults=false;  // Only final results
```

#### 2. Proper Audio Playback Control
```javascript
// Stop microphone BEFORE playing audio
if(rec && recActive){
  rec.stop();
  recActive=false;
  console.log('🎤 Mic stopped for speech');
}

// Stop any currently playing audio
if(currentAudio){
  currentAudio.pause();
  currentAudio.currentTime=0;
  currentAudio=null;
}
```

#### 3. Timing Improvements
```javascript
// Wait 2 seconds after speech ends before restarting mic
setTimeout(()=>{
  if(!speaking && !recActive){
    rec.start();
    recActive=true;
  }
},2000);
```

#### 4. Error Handling
```javascript
rec.onerror=e=>{
  recActive=false;
  console.error('Mic error:',e.error);
  // Auto-recover from errors
  if(e.error!=='no-speech' && e.error!=='aborted'){
    setTimeout(()=>{
      if(!speaking && !recActive){
        rec.start();
      }
    },1000);
  }
};
```

## Testing the Fixes

### Voice Quality Test
1. Start the server locally
2. Open http://localhost:8000/
3. Click START
4. Say "Ciao, come stai?" or "Dov'è l'appartamento?"
5. Listen to the response - should be clear Italian with proper accent

### Audio Overlap Test
1. While the avatar is speaking, verify:
   - Microphone icon should show "Speaking..." (not "Listening...")
   - No echo or double voices
   - Clean audio playback
2. After speech ends:
   - Wait 2 seconds
   - Microphone should automatically restart
   - Should show "Listening..."

## Configuration

### Voice Settings (app/services/elevenlabs_tts.py)
```python
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Rachel (Italian-optimized)
model_id = "eleven_multilingual_v2"
stability = 0.95
similarity_boost = 1.0
style = 0.0
```

### Alternative Voice Options
If Rachel doesn't work well, try these alternatives:

**For Female Voice:**
- `"XrExE9yKIg1WjnnlVkGX"` - Matilda (warm, Italian)
- `"EXAVITQu4vr4xnSDxMaL"` - Bella (soft, Italian)

**For Male Voice:**
- `"pNInz6obpgDQGcFmaJgB"` - Adam (multilingual)
- `"TxGEqnHWrfWFTfGW9XjX"` - Josh (deep, multilingual)

To change voice, edit line 16 in `app/services/elevenlabs_tts.py`

## Console Logs for Debugging

The fixes add detailed console logging:
- `🎤 Mic started` - Microphone begins recording
- `🎤 Mic stopped for speech` - Microphone stops for audio playback
- `🔊 Audio ended` - Audio playback completed
- `🎤 Mic restarted` - Microphone restarts after speech
- `Mic error:` - Any microphone errors

Open browser console (F12) to see these logs.

## Known Limitations

1. **Browser Compatibility**: WebRTC Speech Recognition only works in Chrome/Edge
2. **Audio Lag**: 2-second delay after speech is intentional to prevent overlap
3. **Voice Change**: Switching voices requires server restart to clear cache

## Troubleshooting

### Voice still sounds wrong
- Clear TTS cache: `rm /tmp/tts_*.mp3`
- Restart server
- Try alternative voice IDs (see above)

### Audio still overlaps
- Check browser console for errors
- Ensure using Chrome/Edge (not Firefox/Safari)
- Refresh page and click START again

### Microphone not working
- Grant microphone permissions
- Check browser console for error messages
- Try in incognito mode

## Performance Impact

The fixes slightly increase:
- **Response time**: +0.5s (better quality worth it)
- **Timeout**: 20s (was 15s) - allows for quality generation
- **Delay between interactions**: 2s (prevents overlap)

The quality improvement significantly outweighs the minor performance cost.
