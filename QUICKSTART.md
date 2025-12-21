# Quick Start Guide - Cohen House Concierge

Get Solomon up and running in 5 minutes! 🚀

---

## ⚡ Super Quick Start (For Developers)

```bash
# 1. Clone
git clone https://github.com/CohenNathan/concierge.git
cd concierge

# 2. Install
pip install -r requirements.txt

# 3. Configure
echo "OPENAI_API_KEY=your-key-here" > .env
echo "ELEVENLABS_API_KEY=your-key-here" >> .env

# 4. Run
cd app
uvicorn main:app --reload --port 8000

# 5. Open
# Visit: http://localhost:8000/solomon.html
```

**That's it!** 🎉 Solomon is ready to talk!

---

## 📋 First Time Setup (Step by Step)

### 1. Get API Keys

**OpenAI (Required for AI brain):**
1. Go to https://platform.openai.com/api-keys
2. Sign up or log in
3. Click "Create new secret key"
4. Copy your key (starts with `sk-`)

**ElevenLabs (Required for voice):**
1. Go to https://elevenlabs.io
2. Sign up or log in
3. Go to Profile → API Keys
4. Copy your key

### 2. Install Dependencies

**macOS/Linux:**
```bash
# Install Python 3.9+
python3 --version  # Check if installed

# Install pip packages
pip3 install fastapi uvicorn openai python-dotenv elevenlabs aiohttp
```

**Windows:**
```bash
# Install Python from python.org
python --version  # Check if installed

# Install pip packages
pip install fastapi uvicorn openai python-dotenv elevenlabs aiohttp
```

### 3. Configure Environment

Create `.env` file in the root folder:
```env
OPENAI_API_KEY=sk-your-openai-key-here
ELEVENLABS_API_KEY=your-elevenlabs-key-here
```

### 4. Run the Server

```bash
cd app
python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
✅ Solomon ready
✅ Speech ready
✅ Music controller ready
```

### 5. Open the Interface

In your browser, go to:
```
http://localhost:8000/solomon.html
```

Click **"Activate"** and allow microphone access.

---

## 🎤 Using Solomon

### Start Talking
1. Click "Activate" button
2. Allow microphone when prompted
3. Wait for "Listening" status
4. Speak naturally in Italian or English
5. Solomon will respond with voice and text!

### Try These Commands

**Italian:**
- "Ciao Solomon!" - Say hello
- "Quanto costa BOHO?" - Ask about apartments
- "Dove siete?" - Ask about location
- "Suona musica tradizionale" - Play traditional music
- "Metti musica divertente" - Play fun music

**English:**
- "Hello Solomon!" - Say hello
- "How much is VINTAGE?" - Ask about apartments
- "Where are you located?" - Ask about location
- "Play traditional music" - Play Pizzica
- "Play music" - Open Spotify

---

## 🎵 Music System

Solomon can play music in 3 ways:

### 1. Traditional Pizzica
Say: "Suona musica tradizionale" or "Play traditional music"
- Plays: Pizzica di San Vito (Salento folk dance)

### 2. Fun Songs
Say: "Suona musica divertente" or "Play fun music"
- Plays: Vogliamo le Bambole (fun Italian song)

### 3. Spotify (Manual Selection)
Say: "Metti musica" or "Play music"
- Opens: Spotify app for you to choose

**Note:** Music plays in background, browser stays visible.

---

## 🏠 Cohen House Information

Solomon knows all about Cohen House Taormina:

### Apartments
- **BOHO**: 100m², 10 guests, €500/night, Etna view terrace
- **VINTAGE**: 90m², 8 guests, €450/night, Isola Bella balcony
- **SHABBY**: 90m², 8 guests, €450/night, shabby chic style

### Location
- **Address**: Via Nazionale, Taormina, Sicily
- **Beach**: 20 meters from Isola Bella
- **Supermarket**: Right below the building

### Booking
- **Website**: www.cohenhouse.it
- **Discount**: Save 20-25% with direct booking

---

## 🔧 Troubleshooting

### "Microphone Access Denied"
**Fix:** Allow microphone in browser settings
- Chrome: Settings → Privacy → Site Settings → Microphone
- Safari: Preferences → Websites → Microphone

### "WebSocket Connection Failed"
**Fix:** Check server is running
```bash
cd app
uvicorn main:app --reload --port 8000
```

### "Solomon Not Responding"
**Fix:** Check API keys in `.env` file
```bash
cat .env
# Should show both keys
```

### "Music Not Playing"
**Fix:** Install Spotify app (macOS only)
- Download from https://spotify.com
- Log in to your account

### "No Voice Output"
**Fix:** Check ElevenLabs API key and quota
- Verify key in `.env`
- Check usage at elevenlabs.io

---

## 📱 For Guests

### Using the System
1. Look for the screen with Solomon (the bear)
2. Touch anywhere to activate
3. Speak your question naturally
4. Solomon will answer with voice
5. That's it!

### What to Ask
- "Where is the supermarket?"
- "How do I book?"
- "Play some music"
- "Tell me about the apartments"
- "Do you speak English?"

### Language Support
Solomon speaks:
- 🇮🇹 Italian (Italiano)
- 🇬🇧 English

Just speak in your preferred language!

---

## 🚀 Next Steps

### For Development
- Read the full **README.md** for architecture
- Check **DEPLOYMENT.md** for production setup
- Review **CHANGELOG.md** for features

### For Production
1. Follow **DEPLOYMENT.md** guide
2. Set up HTTPS/SSL
3. Configure domain
4. Monitor logs
5. Set up backups

### For Customization
- Edit `app/openai_assistant.py` for responses
- Modify `app/response_cache.py` for quick answers
- Update `web/solomon.html` for UI changes

---

## 💡 Tips

### Best Practices
- ✅ Speak clearly and naturally
- ✅ Wait for "Listening" status
- ✅ Keep questions focused
- ✅ Use Italian or English only

### What Works Well
- Short, clear questions (5-10 words)
- Normal speaking volume
- Quiet environment (reduce background noise)

### What to Avoid
- Very long questions (15+ words)
- Multiple questions at once
- Whispering or shouting
- Background music while speaking

---

## 📞 Need Help?

**Documentation:**
- README.md - Full documentation
- DEPLOYMENT.md - Production setup
- SYSTEM_STATUS.md - File verification

**Support:**
- Email: info@cohenhouse.com
- Website: www.cohenhouse.it
- GitHub: github.com/CohenNathan/concierge

---

## ✅ System Requirements

### Minimum
- Python 3.9+
- 2GB RAM
- Modern browser (Chrome, Safari, Firefox)
- Microphone
- Internet connection

### Recommended
- Python 3.11+
- 4GB RAM
- Chrome browser (best WebRTC support)
- Good quality microphone
- Fast internet (for Whisper/GPT API)

---

**Ready to go! Enjoy Solomon at Cohen House Taormina! 🏛️🐻✨**
