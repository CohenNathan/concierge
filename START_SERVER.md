# Starting Solomon - Cohen House Concierge

## Quick Start Guide

### 1. Install Dependencies

```bash
pip3 install fastapi uvicorn python-dotenv openai aiohttp pydantic
```

### 2. Configure Environment

Copy `.env.example` to `.env` and add your OpenAI API key:

```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

**Required:**
- `OPENAI_API_KEY` - Get from https://platform.openai.com/api-keys

**Optional (for enhanced features):**
- `ELEVENLABS_API_KEY` - For text-to-speech
- `SERPAPI_KEY` - For web search
- Email settings for notifications
- Azure Face API for recognition

### 3. Start the Server

```bash
# From the concierge directory
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000

# Or run directly
python3 app/main.py
```

### 4. Access Solomon

Open your browser and go to:
- **Main Interface:** http://localhost:8000/
- **API Docs:** http://localhost:8000/docs

## Testing Solomon's Features

Once running, you can test Solomon's enhanced capabilities:

### Ring Doorbell Responses
Ask: "Is Nathan home?" or "È qui Joanna?"
Response: "Nathan and Joanna are not home at the moment, but I can take a message..."

### Website Opening
Say: "Open Cohen House website"
Result: Opens www.cohenhouse.it with direct booking advice

### Travel Planning
- "Show me flights" → Opens Skyscanner with direct booking tips
- "I need a train" → Opens Trenitalia
- "Bus to Catania" → Opens Etna Trasporti

### Knowledge Base
Ask about:
- Cohen House landmarks
- Taormina attractions
- Italian and Sicily history

All responses emphasize **20-25% savings** through direct booking!

## Troubleshooting

**Error: "The api_key client option must be set"**
- Make sure `.env` file exists with valid `OPENAI_API_KEY`

**Port 8000 already in use:**
```bash
# Use a different port
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8001
```

**Import errors:**
- Install missing packages: `pip3 install <package-name>`

## Development Mode

For auto-reload during development:
```bash
python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

🐻 **Solomon е готов да работи!** (Solomon is ready to work!)
