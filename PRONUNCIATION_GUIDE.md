# Italian Pronunciation Guide - Cohen House

## Problem
The property name "Cohen House" was being pronounced with English phonetics, which sounds wrong in Italian.

## Correct Pronunciation

### English vs Italian
- **English**: "Cohen House" (KOH-en House)
- **Italian**: "Koen Haus" (KOH-en Haus)

The Italian pronunciation uses:
- "Koen" instead of "Cohen" (phonetic spelling)
- "Haus" instead of "House" (closer to Italian phonetics)

## Solution Implemented

### Automatic Pronunciation Fix
The TTS system now automatically converts "Cohen House" to "Koen Haus" when speaking in Italian:

```python
def fix_italian_pronunciation(text: str, lang: str) -> str:
    """Fix pronunciation of proper nouns for Italian TTS"""
    if lang == "it":
        # Fix "Cohen House" pronunciation
        text = text.replace("Cohen House", "Koen Haus")
        text = text.replace("cohen house", "Koen Haus")
        text = text.replace("Cohen house", "Koen Haus")
        text = text.replace("COHEN HOUSE", "Koen Haus")
    return text
```

This function is called BEFORE sending text to the TTS engine, ensuring proper Italian pronunciation.

## Technical Details

### Implementation
1. **Location**: `app/services/elevenlabs_tts.py`
2. **Function**: `fix_italian_pronunciation()`
3. **Applied**: Before TTS generation
4. **Cache Impact**: Different pronunciation = different cache key

### Why This Works
- ElevenLabs TTS engine respects phonetic spelling
- "Koen Haus" is pronounced correctly by Italian voice
- Native Italian speakers will hear it naturally
- English pronunciation artifacts are eliminated

## Testing

### How to Verify
1. Clear TTS cache: `rm /tmp/tts_*.mp3`
2. Restart server
3. Say: "Dov'è Cohen House?" or "Dimmi di Cohen House"
4. Listen for "Koen Haus" pronunciation (Italian phonetics)

### Expected Result
The voice should say "Koen Haus" with Italian pronunciation, not "Cohen House" with English pronunciation.

## Other Pronunciation Fixes

This system can be extended for other proper nouns:

```python
# Example additions:
text = text.replace("Taormina", "Taormina")  # Already correct
text = text.replace("Isola Bella", "Isola Bella")  # Already correct
text = text.replace("Mount Etna", "Monte Etna")  # Italian version
```

## Notes

- Only applies to Italian language (`lang == "it"`)
- English responses keep original "Cohen House" pronunciation
- Cache key includes the modified text to prevent conflicts
- Can be disabled by removing the function call if needed

## Troubleshooting

### Still hearing English pronunciation?
1. **Clear cache**: `rm /tmp/tts_*.mp3` (REQUIRED!)
2. **Restart server**: Old cache will persist otherwise
3. **Check logs**: Look for "🎤 Generating TTS [it] with Matilda: Koen Haus"
4. **Verify code**: Ensure `fix_italian_pronunciation()` is being called

### Want to add more fixes?
Edit `app/services/elevenlabs_tts.py` and add more replacements in the `fix_italian_pronunciation()` function.
