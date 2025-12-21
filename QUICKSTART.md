# 🐻 Cohen House Bear - Quick Start Guide

## Installation

### Step 1: Install Dependencies

**Option A: Using the setup script (Recommended)**
```bash
./setup.sh
```

**Option B: Manual installation**
```bash
# Install dependencies
pip3 install -r requirements.txt

# Or with virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 2: Configure API Keys

Create a `.env` file in the project root:

```bash
# Create .env file
cp .env.example .env  # Or create manually
```

Edit `.env` and add your API keys:
```env
OPENAI_API_KEY=sk-your-openai-key-here
ELEVENLABS_API_KEY=your-elevenlabs-key-here
```

**Get API Keys:**
- OpenAI: https://platform.openai.com/api-keys
- ElevenLabs: https://elevenlabs.io/app/settings/api-keys

### Step 3: Start the Application

```bash
# Start the server
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Step 4: Open in Browser

Navigate to: http://localhost:8000

## Troubleshooting

### "No module named uvicorn"

This means dependencies are not installed. Run:
```bash
pip3 install -r requirements.txt
```

If you're using a virtual environment, make sure it's activated:
```bash
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

### "No module named app.main"

Make sure you're in the project root directory:
```bash
cd /path/to/concierge
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### API Key Errors

Make sure your `.env` file exists and contains valid API keys:
```bash
cat .env  # Check if file exists and has keys
```

### Port Already in Use

If port 8000 is busy, use a different port:
```bash
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8080
```

## Testing the Installation

Run the test script to verify everything is working:
```bash
python3 start_bear.py
```

This will check:
- ✅ All modules import correctly
- ✅ FastAPI app is configured
- ✅ Language support works
- ✅ Action mappings are correct

## Commands Reference

### Start Server
```bash
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Start with Auto-Reload (Development)
```bash
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Test Installation
```bash
python3 start_bear.py
```

### Run Tests
```bash
python3 test_code_logic.py
```

## macOS Specific Notes

On macOS, you might need to install additional dependencies:

```bash
# If you get SSL errors
pip3 install --upgrade certifi

# If face-recognition fails to install
brew install cmake
pip3 install dlib
pip3 install face-recognition
```

## Language Support

The bear understands:
- 🇮🇹 **Italian**: "Ciao", "Suona la pizzica", "Apri Spotify"
- 🇬🇧 **English**: "Hello", "Play music", "Open Spotify"

## Need Help?

Check the full documentation: `README.md`

For issues, visit: https://github.com/CohenNathan/concierge/issues
