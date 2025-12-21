#!/bin/bash

# Cohen House Concierge - Setup Script
# This script installs all dependencies and sets up the environment

set -e  # Exit on error

echo "🐻 Cohen House Bear - Setup Script"
echo "=" 
echo ""

# Check Python version
echo "📋 Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d ' ' -f 2)
echo "✅ Found Python $PYTHON_VERSION"

# Check pip
echo ""
echo "📋 Checking pip..."
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3."
    exit 1
fi
echo "✅ pip3 is available"

# Create virtual environment (optional but recommended)
echo ""
echo "🔧 Setting up virtual environment (optional)..."
read -p "Create virtual environment? (recommended) [Y/n]: " CREATE_VENV
CREATE_VENV=${CREATE_VENV:-Y}

if [[ $CREATE_VENV =~ ^[Yy]$ ]]; then
    if [ ! -d "venv" ]; then
        echo "Creating virtual environment..."
        python3 -m venv venv
    fi
    
    echo "Activating virtual environment..."
    source venv/bin/activate
    echo "✅ Virtual environment activated"
    echo ""
    echo "ℹ️  To activate in future sessions, run:"
    echo "   source venv/bin/activate"
else
    echo "⚠️  Skipping virtual environment (installing globally)"
fi

# Install dependencies
echo ""
echo "📦 Installing Python dependencies..."
echo "This may take a few minutes..."
pip3 install -r requirements.txt

# Check if .env exists
echo ""
echo "🔐 Checking for .env file..."
if [ ! -f ".env" ]; then
    echo "⚠️  No .env file found"
    echo ""
    echo "Creating .env template..."
    cat > .env << 'EOF'
# Cohen House Concierge - Environment Variables
# Copy this file and add your real API keys

# OpenAI API Key (required for AI responses)
OPENAI_API_KEY=your_openai_api_key_here

# ElevenLabs API Key (required for text-to-speech)
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here

# Optional: Grok API Key (for alternative AI)
# GROK_API_KEY=your_grok_api_key_here
EOF
    echo "✅ Created .env template"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env and add your real API keys!"
    echo "   - Get OpenAI key from: https://platform.openai.com/api-keys"
    echo "   - Get ElevenLabs key from: https://elevenlabs.io/app/settings/api-keys"
else
    echo "✅ .env file exists"
fi

# Test installation
echo ""
echo "🧪 Testing installation..."
python3 start_bear.py > /tmp/bear_test.log 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Installation test passed!"
else
    echo "⚠️  Installation test had warnings (check /tmp/bear_test.log)"
fi

# Final instructions
echo ""
echo "=" 
echo "🎉 Setup Complete!"
echo "=" 
echo ""
echo "📋 Next Steps:"
echo ""
echo "1. Edit .env file with your API keys:"
echo "   nano .env"
echo ""
echo "2. Start the bear application:"
if [[ $CREATE_VENV =~ ^[Yy]$ ]]; then
    echo "   source venv/bin/activate  # (if not already activated)"
fi
echo "   python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000"
echo ""
echo "3. Open browser to:"
echo "   http://localhost:8000"
echo ""
echo "📚 For more info, see README.md"
echo ""
