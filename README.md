# Cohen House Concierge 🏛️🤖

AI-powered smart concierge system for Cohen House Taormina, Sicily. Solomon, the magical AI bear, provides 24/7 guest assistance with multilingual support, music control, and intelligent conversation.

**Production-Ready** - December 2025

---

## 🎯 System Overview

Cohen House Concierge is a sophisticated AI system that:
- Provides instant answers about Cohen House apartments
- Responds in Italian and English with natural conversation
- Controls music and entertainment systems
- Uses voice recognition with Whisper AI
- Features a beautiful 3D avatar interface
- Caches responses for lightning-fast replies

---

## 📁 Key Files and Architecture

### Core AI Components (`/app`)

#### **openai_assistant.py** - Main AI Logic
- GPT-4o-mini powered conversation engine
- Exact apartment facts (BOHO, VINTAGE, SHABBY)
- Music triggers and action handling
- Language detection and response generation
- Custom Solomon personality

#### **openai_speech.py** - Whisper Speech Recognition
- Whisper-1 model for audio transcription
- Anti-spam filters (blocks YouTube/social media noise)
- Latin alphabet enforcement
- Language detection (Italian/English)
- Quality filters for transcription

#### **response_cache.py** - Quick Response System
- Instant replies for common questions
- Pre-cached answers for speed
- Keyword matching system
- Reduces API calls and improves response time

#### **spotify_control.py** - Music Controller
- Plays traditional Pizzica di San Vito
- Plays fun songs (Vogliamo le Bambole)
- Opens Spotify for guest selection
- Invisible background playback
- Keeps browser visible while playing music

### Frontend (`/web`)

#### **solomon.html** - Main UI
- Professional Cohen House branding
- 3D bear avatar (Solomon) with Three.js
- Real-time voice interaction
- WebSocket communication
- High-quality audio recording (48kHz)
- Elegant gold/black luxury design

### Server (`/app`)

#### **main.py** - FastAPI Server
- WebSocket endpoint for real-time chat
- Audio upload endpoint for Whisper
- Integration with all AI components
- Handles actions (music, browser control)
- Booking system integration

#### **elevenlabs_tts.py** - Text-to-Speech
- Natural voice synthesis
- Supports Italian and English
- Cached audio files for performance

#### **browser_control.py** - Web Automation
- Opens useful websites (Etna tours, Trenitalia, etc.)
- Helps guests with bookings and information

---

## 🏠 Cohen House Apartments

The system knows these exact facts:

### BOHO Apartment
- **Size:** 100m²
- **Capacity:** 10 guests
- **Price:** €500/night
- **Style:** Bohemian design
- **Feature:** Terrace with Etna view

### VINTAGE Apartment
- **Size:** 90m²
- **Capacity:** 8 guests
- **Price:** €450/night
- **Style:** Baroque elegance
- **Feature:** Balcony overlooking Isola Bella

### SHABBY Apartment
- **Size:** 90m²
- **Capacity:** 8 guests
- **Price:** €450/night
- **Style:** Shabby chic with pastels
- **Feature:** Charming coastal vibe

**Location:** Via Nazionale, 20 meters from Isola Bella beach  
**Supermarket:** Right below Cohen House  
**Booking:** Direct booking at www.cohenhouse.it saves 20-25%

---

## 🚀 Setup and Installation

### Prerequisites
- Python 3.9+
- Node.js 16+
- OpenAI API key
- ElevenLabs API key (for TTS)
- Spotify account (for music features)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/CohenNathan/concierge.git
cd concierge
```

2. **Install Python dependencies:**
```bash
pip install -r requirements.txt
# Main packages: fastapi, uvicorn, openai, python-dotenv
```

3. **Install Node.js dependencies:**
```bash
npm install
```

4. **Set up environment variables:**
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

5. **Run the server:**
```bash
cd app
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

6. **Open the interface:**
Navigate to `http://localhost:8000/solomon.html`

---

## 🎵 Music System

Solomon can play music in three ways:

1. **Traditional Pizzica** - "Suona musica tradizionale"
   - Pizzica di San Vito (Salento traditional dance)
   
2. **Fun Songs** - "Suona musica divertente"
   - Vogliamo le Bambole (fun Italian song)
   
3. **Spotify Control** - "Metti musica"
   - Opens Spotify app for manual selection

Music plays in the background while keeping the browser visible.

---

## 🗂️ File Structure

```
concierge/
├── app/                          # Backend application
│   ├── openai_assistant.py       # ✅ Main AI logic
│   ├── openai_speech.py          # ✅ Whisper transcription
│   ├── response_cache.py         # ✅ Quick responses
│   ├── spotify_control.py        # ✅ Music control
│   ├── main.py                   # FastAPI server
│   ├── elevenlabs_tts.py         # Text-to-speech
│   ├── browser_control.py        # Web automation
│   └── booking.py                # Booking system
├── web/                          # Frontend files
│   ├── solomon.html              # ✅ Main UI with audio fix
│   └── avatar.glb                # 3D bear model
├── static/                       # Static assets
├── deploy.sh                     # ✅ SSH deployment script (Linux/macOS)
├── deploy.bat                    # ✅ SSH deployment script (Windows)
├── deploy.config.example         # ✅ Deployment configuration template
├── SSH_DEPLOYMENT_GUIDE.md       # ✅ SSH deployment guide (BG/EN)
├── .gitignore                    # ✅ Ignores TTS cache, backups
├── package.json                  # Node dependencies
└── README.md                     # This file
```

---

## 🔒 Security and Privacy

### .gitignore Configuration
The system excludes:
- TTS audio cache (`tts_*.mp3`, `audio_cache/`)
- Backup files (`*.backup`, `*.OLD`, `*.broken`)
- Environment variables (`.env`)
- Python cache (`__pycache__/`)
- Database files (`*.db`, `*.sqlite3`)
- Face recognition data (`*.pkl`, `*.dat`)

### API Keys
Never commit API keys. Use `.env` file for secrets:
- OpenAI API key
- ElevenLabs API key
- Ring doorbell credentials (if used)

---

## 🧪 Testing

### Test Files
- `test_openai.py` - Tests OpenAI integration
- `test_ring.py` - Tests Ring doorbell integration

Run tests:
```bash
python test_openai.py
python test_ring.py
```

---

## 📦 Deployment

### Quick SSH/CLI Deployment (Recommended)

The easiest way to deploy to a remote server via SSH:

```bash
# 1. Run deployment script
./deploy.sh

# 2. Edit configuration (first time only)
nano deploy.config
# Add your server SSH details

# 3. Deploy!
./deploy.sh
```

**Windows users:** Use `deploy.bat` instead

**Full Guide:** See [SSH_DEPLOYMENT_GUIDE.md](SSH_DEPLOYMENT_GUIDE.md) for complete instructions in Bulgarian and English.

### Production Deployment Checklist

1. **Server Requirements:**
   - Linux/macOS server
   - Python 3.9+
   - Minimum 2GB RAM
   - HTTPS certificate (for secure WebSocket)

2. **Environment Setup:**
   - Set production environment variables
   - Configure firewall (allow port 8000 or 443)
   - Set up reverse proxy (nginx/Apache)

3. **Process Management:**
   ```bash
   # Using systemd or supervisor
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
   ```

4. **Domain Configuration:**
   - Point domain to server IP
   - Configure SSL certificate
   - Update WebSocket URL in `solomon.html`

**Detailed Guide:** See [DEPLOYMENT.md](DEPLOYMENT.md) for step-by-step production deployment instructions.

---

## 🔧 Maintenance

### Backup Strategy

1. **Code Backup:**
   - GitHub repository (automatic)
   - Regular commits to main branch

2. **Data Backup:**
   - Face recognition data (if used)
   - Booking database
   - Custom responses

3. **Configuration Backup:**
   - `.env` file (store securely, not in git)
   - API keys documentation
   - Server configuration files

### Monitoring

- Check server logs regularly
- Monitor API usage (OpenAI, ElevenLabs)
- Test audio system weekly
- Verify WebSocket connections

---

## 🐛 Troubleshooting

### Common Issues

**WebSocket Connection Failed:**
- Check server is running on correct port
- Verify firewall allows WebSocket connections
- Ensure URL matches server address

**Microphone Not Working:**
- Browser requires HTTPS for microphone access
- Check browser permissions
- Verify audio recording settings (48kHz, opus codec)

**Music Not Playing:**
- Ensure Spotify is installed
- Check macOS permissions for automation
- Verify AppleScript execution is allowed

**TTS Not Working:**
- Check ElevenLabs API key
- Verify API quota hasn't been exceeded
- Check audio file permissions

**No Voice Recognition:**
- Verify OpenAI API key is valid
- Check audio file size (minimum 30KB)
- Ensure audio quality settings are correct

---

## 🌟 Features

### Current Features
✅ Voice recognition (Whisper)  
✅ Multilingual support (Italian, English)  
✅ Music control (Spotify integration)  
✅ Quick response caching  
✅ 3D avatar interface  
✅ Real-time WebSocket communication  
✅ Anti-spam filters  
✅ Professional Cohen House branding  

### Removed/Deprecated
❌ Old three.js imports (now using CDN)  
❌ face-api library (facial recognition not in use)  
❌ Old backup files cleaned  

---

## 👥 Team Collaboration

### For Developers

1. **Branch Strategy:**
   - `main` - production-ready code
   - `dev` - development work
   - Feature branches for new work

2. **Commit Guidelines:**
   - Clear commit messages
   - Test before pushing
   - Document API changes

3. **Code Style:**
   - Follow PEP 8 for Python
   - Use async/await for I/O operations
   - Add comments for complex logic

### For Content Team

- Update apartment facts in `openai_assistant.py`
- Modify quick responses in `response_cache.py`
- Adjust Solomon's personality in system prompts

---

## 📞 Support

**Technical Issues:**  
info@cohenhouse.com

**Cohen House Taormina:**  
Via Nazionale, Taormina, Sicily  
www.cohenhouse.it

---

## 📜 License

Proprietary - Cohen House Taormina © 2025

---

## 🎉 Status: Production Ready

**Last Updated:** December 21, 2025

✅ All core files in repository  
✅ Security configured (.gitignore)  
✅ Audio system optimized  
✅ Ready for real guests  
✅ Ready for deployment  
✅ Ready for team collaboration  
✅ Ready for backup and maintenance  

---

**Built with ❤️ for Cohen House Taormina**
