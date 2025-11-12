#!/bin/bash
# Simple script to run the CloseAI web application

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "Please create a .env file based on .env.example"
    echo "You need to add your OPENAI_API_KEY"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate 2>/dev/null || . venv/Scripts/activate 2>/dev/null

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt

# Run the application
echo "🚀 Starting CloseAI web server..."
echo "🌐 Open your browser at http://localhost:5000"
echo ""
python app.py
