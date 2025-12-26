"""
Professional audio preprocessing to filter noise before Whisper
"""
import io
import numpy as np
from pydub import AudioSegment
from pydub.silence import detect_nonsilent

def preprocess_audio(audio_bytes: bytes) -> bytes:
    """
    Clean audio before sending to Whisper:
    1. Remove silence
    2. Normalize volume
    3. Filter background noise
    """
    try:
        # Load audio
        audio = AudioSegment.from_file(io.BytesIO(audio_bytes))
        
        # Convert to mono if stereo
        if audio.channels > 1:
            audio = audio.set_channels(1)
        
        # Normalize volume
        audio = audio.normalize()
        
        # Detect non-silent chunks (voice activity detection)
        nonsilent_ranges = detect_nonsilent(
            audio,
            min_silence_len=300,  # 300ms of silence
            silence_thresh=audio.dBFS - 16  # Threshold
        )
        
        # If no speech detected, return None
        if not nonsilent_ranges:
            print("❌ No speech detected in audio")
            return None
        
        # Extract only non-silent parts
        speech_chunks = [audio[start:end] for start, end in nonsilent_ranges]
        if not speech_chunks:
            return None
            
        # Combine speech chunks
        processed = speech_chunks[0]
        for chunk in speech_chunks[1:]:
            processed += chunk
        
        # Check minimum duration (prevent very short noise)
        if len(processed) < 500:  # Less than 0.5 seconds
            print(f"❌ Audio too short: {len(processed)}ms")
            return None
        
        # Check maximum duration (prevent long TV/YouTube)
        if len(processed) > 10000:  # More than 10 seconds
            print(f"❌ Audio too long: {len(processed)}ms (likely background TV)")
            return None
        
        # Export processed audio
        output = io.BytesIO()
        processed.export(output, format="wav")
        return output.getvalue()
        
    except Exception as e:
        print(f"❌ Audio preprocessing error: {e}")
        return audio_bytes  # Return original if preprocessing fails
