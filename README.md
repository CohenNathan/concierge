# Cohen House Concierge - Solomon the Bear 🐻

An AI-powered concierge system featuring Solomon, a friendly bear assistant that helps guests at Cohen House in Taormina, Sicily.

## Features

- **Multilingual Support**: Solomon speaks Italian and English
- **Voice Recognition**: Understands voice commands via Whisper API
- **Text-to-Speech**: Responds with natural voice using ElevenLabs
- **Smart Actions**: Controls music (Spotify), opens websites, and provides information
- **Face Recognition**: Recognizes returning guests
- **Ring Doorbell Integration**: Greets guests at the door

## Architecture

### Main Components

- **FastAPI Backend** (`app/main.py`): WebSocket server handling real-time communication
- **OpenAI Assistant** (`app/openai_assistant.py`): Natural language processing with GPT-4o-mini
- **Speech Recognition** (`app/openai_speech.py`): Transcribes audio using Whisper API
- **Text-to-Speech** (`app/elevenlabs_tts.py`): Generates voice responses with ElevenLabs
- **Spotify Control** (`app/spotify_control.py`): Plays traditional Pizzica music
- **Web Interface** (`web/solomon.html`): 3D animated bear with voice interaction

## Language Support

Solomon supports both Italian and English:

### Italian Commands
- "Suona la pizzica tradizionale" → Plays traditional Pizzica di San Vito
- "Metti musica divertente" → Plays fun music
- "Apri Spotify" → Opens Spotify app
- "Dimmi degli appartamenti" → Provides apartment information

### English Commands
- "Play traditional tarantella" → Plays traditional Pizzica di San Vito
- "Play fun music" → Plays fun music
- "Open Spotify" → Opens Spotify app
- "Tell me about the apartments" → Provides apartment information

## Action System

Solomon can perform the following actions:

- `play_pizzica` - Plays traditional Pizzica di San Vito music
- `play_bambole` - Plays fun music (Vogliamo le Bambole)
- `open_spotify` - Opens Spotify app for guest to choose music
- `open_etna` - Opens information about Mount Etna tours
- `open_trenitalia` - Opens Trenitalia website for train tickets
- `open_skyscanner` - Opens Skyscanner for flight bookings

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables in `.env`:
```
OPENAI_API_KEY=your_openai_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

3. Run the server:
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

4. Open browser:
```
http://localhost:8000
```

## Testing

Run the code logic tests:
```bash
python3 test_code_logic.py
```

This verifies:
- Italian keyword detection
- English keyword detection
- Action mapping consistency
- Language support

## Project Structure

```
concierge/
├── app/
│   ├── main.py                    # FastAPI server
│   ├── openai_assistant.py        # AI assistant with GPT-4o-mini
│   ├── openai_speech.py           # Speech recognition with Whisper
│   ├── elevenlabs_tts.py          # Text-to-speech with ElevenLabs
│   ├── spotify_control.py         # Music playback control
│   ├── browser_control.py         # Website opening control
│   ├── face_recognition_system.py # Guest face recognition
│   ├── ring_client.py             # Ring doorbell integration
│   └── ...                        # Other supporting modules
├── web/
│   ├── solomon.html               # Main web interface
│   ├── avatar.glb                 # 3D bear model
│   └── ...                        # Other web assets
├── requirements.txt               # Python dependencies
├── test_code_logic.py            # Unit tests
└── README.md                      # This file
```

## Cohen House Information

Solomon provides accurate information about Cohen House apartments:

### Apartments
- **BOHO**: 100m², 10 guests, €500/night, bohemian style, terrace with Etna view
- **VINTAGE**: 90m², 8 guests, €450/night, baroque style, balcony over Isola Bella
- **SHABBY**: 90m², 8 guests, €450/night, shabby chic, pastel colors

### Location
- Address: Via Nazionale, Taormina
- Distance to beach: 20 meters from Isola Bella
- Supermarket: Located below Cohen House

### Booking
Save 20-25% by booking directly at: www.cohenhouse.it

## Development

The project uses:
- **Python 3.12+**
- **FastAPI** for web server
- **OpenAI GPT-4o-mini** for natural language understanding
- **Whisper API** for speech recognition
- **ElevenLabs** for text-to-speech
- **Three.js** for 3D bear animation
- **WebSocket** for real-time communication

## License

Proprietary - Cohen House Taormina

## Contact

For questions or support:
- Email: info@cohenhouse.com
- Phone: +393478879992
