#!/bin/bash

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║        Cohen House Concierge - Voice Cache Clear              ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Count cached files
COUNT=$(ls /tmp/tts_*.mp3 2>/dev/null | wc -l)

if [ $COUNT -eq 0 ]; then
    echo "✅ No cached voice files found - cache is already clean"
else
    echo "🗑️  Found $COUNT cached voice files"
    echo "   Removing..."
    rm /tmp/tts_*.mp3
    echo "✅ Cache cleared successfully"
fi

echo ""
echo "🔍 Verifying voice configuration..."
VOICE_ID=$(grep "^VOICE_ID" app/services/elevenlabs_tts.py | cut -d'"' -f2)
echo "   Current voice ID: $VOICE_ID"

if [ "$VOICE_ID" = "XrExE9yKIg1WjnnlVkGX" ]; then
    echo "   ✅ Using Matilda (native Italian) - CORRECT"
elif [ "$VOICE_ID" = "21m00Tcm4TlvDq8ikWAM" ]; then
    echo "   ⚠️  Using Rachel (has English accent) - SHOULD UPDATE"
    echo "   Run: Update app/services/elevenlabs_tts.py line 16 to:"
    echo "   VOICE_ID = \"XrExE9yKIg1WjnnlVkGX\""
else
    echo "   ⚠️  Using unknown voice: $VOICE_ID"
fi

echo ""
echo "📋 Next steps:"
echo "   1. Restart server: uvicorn app.main:app --reload --port 8000"
echo "   2. Open http://localhost:8000/"
echo "   3. Click START"
echo "   4. Say 'Ciao, come stai?'"
echo "   5. Listen - should be native Italian, not English accent"
echo ""
echo "🐛 Debug: Open browser console (F12) to see:"
echo "   '🎤 Generating TTS [it] with Matilda: ...'"
echo ""
