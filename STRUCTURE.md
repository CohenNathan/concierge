# Cohen House Concierge - Project Structure

## Overview
This document describes the reorganized project structure following best practices for Python applications.

## Directory Structure

```
app/
├── api/                          # API integrations
│   ├── __init__.py
│   ├── openai_assistant.py      # OpenAI GPT Assistant integration
│   └── openai_speech.py         # OpenAI Whisper speech recognition
├── services/                     # Core services
│   ├── __init__.py
│   ├── elevenlabs_tts.py        # ElevenLabs text-to-speech
│   ├── face_recognition_system.py
│   ├── doorbell_handler.py      # Ring doorbell integration
│   └── spotify_control.py       # Spotify music control
├── handlers/                     # Request handlers
│   ├── __init__.py
│   ├── actions.py               # Action handlers
│   ├── booking.py               # Booking API endpoints
│   └── search.py                # Search functionality
├── utils/                        # Utilities
│   ├── __init__.py
│   ├── browser_control.py       # Browser automation
│   ├── window_manager.py        # Window management
│   └── response_cache.py        # Response caching
├── config/                       # Configuration
│   ├── __init__.py
│   └── constants.py             # Application constants
└── main.py                       # FastAPI entry point

web/                              # Web interface
├── index.html                    # Main page
├── favicon.ico
├── assets/
│   ├── models/
│   │   └── avatar.glb           # 3D avatar model
│   └── js/
│       └── ring-listener.js     # Ring doorbell listener
└── README.md

known_faces/                      # Face recognition data
static/                           # Static assets

Configuration files:
├── .env.example                  # Environment variables template
├── .gitignore                    # Git ignore rules
├── requirements.txt              # Python dependencies
├── package.json                  # Node.js dependencies
└── Documentation (*.md files)
```

## Import Changes

After reorganization, imports should be updated as follows:

### Old imports:
```python
from app.openai_assistant import assistant
from app.elevenlabs_tts import text_to_speech
from app.spotify_control import spotify
from app.browser_control import browser
from app.response_cache import get_quick_response
from app.booking import router as booking_router
```

### New imports:
```python
from app.api.openai_assistant import assistant
from app.services.elevenlabs_tts import text_to_speech
from app.services.spotify_control import spotify
from app.utils.browser_control import browser
from app.utils.response_cache import get_quick_response
from app.handlers.booking import router as booking_router
```

## Benefits of New Structure

1. **Better Organization**: Code is grouped by functionality
2. **Easier Navigation**: Developers can quickly find related code
3. **Scalability**: Easy to add new modules in appropriate directories
4. **Maintainability**: Clear separation of concerns
5. **Testing**: Easier to write and organize tests

## Migration Notes

- All imports in `app/main.py` have been updated
- Test files have been updated with new import paths
- Web assets organized in `web/assets/` subdirectories
- Backup and test HTML files removed from `web/`
- Configuration constants extracted to `app/config/constants.py`

