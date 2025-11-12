# 🚀 Quick Start Guide

This guide will help you get CloseAI up and running in minutes!

## Prerequisites

Before you begin, make sure you have:
- Python 3.8+ installed
- An OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

## Step-by-Step Setup

### 1. Get the Code

```bash
git clone https://github.com/SergioNietoP/closeAI.git
cd closeAI
```

### 2. Set Up Your API Key

Create a `.env` file:
```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
SECRET_KEY=any-random-string-for-flask-sessions
```

### 3. Quick Start (Easiest Way)

**On Linux/Mac:**
```bash
./run.sh
```

**On Windows:**
```bash
python app.py
```

### 4. Manual Setup (Alternative)

If you prefer to set things up manually:

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

### 5. Open Your Browser

Navigate to: **http://localhost:5000**

## 🎉 You're Done!

You should now see the CloseAI homepage. Try out the different tools:
- 🎤 Interview Evaluator
- ❓ Question Generator  
- 📝 Text Analyzer
- 💬 AI Chat

## 💡 Tips

- **First Time Using**: Start with the Chat tool to test your API key
- **API Costs**: Remember that using the tools will consume OpenAI API credits
- **Development**: The app runs in debug mode by default for easy testing
- **Errors**: If you see API errors, check your `.env` file and API key

## 🆘 Troubleshooting

### "ModuleNotFoundError"
Make sure you installed dependencies: `pip install -r requirements.txt`

### "OpenAI API Error"
- Check your API key in `.env`
- Verify you have credits in your OpenAI account
- Make sure your API key starts with `sk-`

### "Port 5000 already in use"
Change the port in `.env`:
```
PORT=8000
```

## 📚 Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Explore the original examples in the `Examples/` directory
- Check out the API endpoints documentation in README.md
- Customize the web interface in `templates/` and `static/`

Happy experimenting with AI! 🤖
