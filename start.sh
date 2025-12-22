#!/bin/bash

# Solomon - Cohen House Concierge Startup Script
# Usage: ./start.sh

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║         Solomon - Cohen House Concierge Starting...         ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  .env file not found!"
    echo ""
    echo "Creating .env from .env.example..."
    if [ -f .env.example ]; then
        cp .env.example .env
        echo "✅ .env file created"
        echo ""
        echo "⚠️  IMPORTANT: Edit .env and add your OPENAI_API_KEY"
        echo "   Get your key from: https://platform.openai.com/api-keys"
        echo ""
        read -p "Press Enter after you've added your API key to .env..."
    else
        echo "❌ .env.example not found. Please create .env manually."
        exit 1
    fi
fi

# Check if OPENAI_API_KEY is set in .env
if ! grep -q "OPENAI_API_KEY=sk-" .env; then
    echo "⚠️  OPENAI_API_KEY not configured in .env"
    echo "   Please edit .env and add your OpenAI API key"
    echo ""
    read -p "Press Enter to continue anyway (server will fail) or Ctrl+C to exit..."
fi

# Check if required packages are installed
echo "🔍 Checking dependencies..."
python3 -c "import fastapi, uvicorn, openai" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  Some dependencies are missing"
    echo "📦 Installing required packages..."
    pip3 install fastapi uvicorn python-dotenv openai aiohttp pydantic
    echo ""
fi

echo "✅ Dependencies ready"
echo ""
echo "🚀 Starting Solomon..."
echo "   Access at: http://localhost:8000"
echo "   API Docs:  http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""
echo "─────────────────────────────────────────────────────────────"
echo ""

# Start the server
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000
