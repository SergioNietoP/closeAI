# 🤖 CloseAI - AI Experimentation Platform

An interactive web-based platform for experimenting with various AI capabilities powered by OpenAI's APIs. This project showcases practical applications of AI including interview evaluation, question generation, text analysis, and conversational AI.

## 🌟 Features

### Web Interface
- **Modern, Responsive Design**: Clean and intuitive UI that works on all devices
- **Interactive Tools**: Four main AI-powered tools accessible through the web interface
- **Real-time Processing**: Get instant AI-powered insights and analysis

### AI Tools

1. **🎤 Interview Evaluator**
   - Evaluate interview responses with AI
   - Get detailed scores on multiple metrics (Creativity, Communication, Problem-Solving, etc.)
   - Receive comprehensive feedback with pros and cons

2. **❓ Question Generator**
   - Generate comprehensive assessment questions for any topic
   - Create structured evaluations with multiple topics and subtopics
   - Perfect for educators and HR professionals

3. **📝 Text Analyzer**
   - Analyze text for sentiment, grammar, and style
   - Get AI-powered summaries and insights
   - Multiple analysis types: general, sentiment, grammar check, summarization

4. **💬 AI Chat**
   - Interactive chat interface with AI assistant
   - Context-aware conversations
   - Get help, ask questions, or explore various topics

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SergioNietoP/closeAI.git
   cd closeAI
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   SECRET_KEY=your_secret_key_here
   ```

### Running the Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Open your browser**
   
   Navigate to `http://localhost:5000`

3. **Start exploring!**
   
   Try out the different AI tools through the web interface.

## 📁 Project Structure

```
closeAI/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore file
├── templates/                 # HTML templates
│   ├── base.html             # Base template
│   ├── index.html            # Homepage
│   ├── interview_evaluator.html
│   ├── question_generator.html
│   ├── text_analyzer.html
│   ├── chat.html
│   ├── 404.html
│   └── 500.html
├── static/                    # Static files
│   ├── css/
│   │   └── style.css         # Main stylesheet
│   └── js/
│       ├── main.js           # Common utilities
│       ├── interview.js      # Interview evaluator logic
│       ├── questions.js      # Question generator logic
│       ├── analyzer.js       # Text analyzer logic
│       └── chat.js           # Chat interface logic
├── Examples/                  # Original example scripts
│   ├── test_approach/        # Test scripts
│   ├── content_generation/   # Content generation examples
│   └── external_scripts/     # External integrations
├── audios/                    # Audio files for testing
├── Bitacora/                  # Development logs
└── README.md                  # This file
```

## 🛠️ Technology Stack

- **Backend**: Python 3.8+, Flask 3.0
- **AI**: OpenAI GPT-3.5-turbo, Whisper API
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Custom CSS with modern gradients and animations
- **Deployment**: Gunicorn-ready

## 📚 API Endpoints

### POST /api/evaluate-answer
Evaluate an interview answer.

**Request:**
```json
{
  "question": "Interview question",
  "answer": "Candidate's answer"
}
```

### POST /api/generate-questions
Generate assessment questions.

**Request:**
```json
{
  "topics": [
    {
      "title": "Topic name",
      "description": "Topic description"
    }
  ]
}
```

### POST /api/analyze-text
Analyze text with AI.

**Request:**
```json
{
  "text": "Text to analyze",
  "type": "general|sentiment|grammar|summary"
}
```

### POST /api/chat
Send a chat message to AI.

**Request:**
```json
{
  "message": "Your message",
  "history": []
}
```

## 🧪 Original Examples

The `Examples/` directory contains the original Python scripts that inspired this web platform:

- **test_approach/**: Interview evaluation and audio transcription scripts
- **content_generation/**: Content creation and manipulation
- **external_scripts/**: Wikipedia scraping and data processing notebooks

## 🔐 Security Notes

- Never commit your `.env` file or expose your API keys
- The `.gitignore` file is configured to exclude sensitive files
- Use environment variables for all configuration
- Consider rate limiting for production deployments

## 📝 Release History

* **1.0.0** - Major Update
    * Web interface with Flask backend
    * Four interactive AI tools
    * Modern, responsive design
    * API endpoints for all features
* 0.2.1
    * Ask PDF
* 0.2.0
    * Get Chapters PDF
    * PDF input
    * Generate Questions 
* 0.1.1
    * Obtain Manual Content
* 0.1.0
    * Wikipedia Scrap
    * Test LinkedIn Web Scraping
* 0.0.1
    * Test generate QA
    * Coding evaluation using API
    * Whisper approach (more dynamic evaluation)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📖 Documentation & Resources

- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Deep Learning](https://www.deeplearning.ai/short-courses/)
- [MiniLM](https://github.com/microsoft/unilm/tree/master/minilm)
- [LLama2](https://ai.meta.com/llama/)
- [Transformers](https://huggingface.co/docs/transformers/index)
- [Models OpenAI](https://platform.openai.com/docs/models)
- [Whisper API](https://openai.com/research/whisper)
- [Embeddings OpenAI](https://platform.openai.com/docs/guides/embeddings)
- [LangChain](https://python.langchain.com/docs/get_started/introduction.html)
- [PineCone](https://www.pinecone.io/)
- [Chroma](https://www.trychroma.com/)

## 📄 License

This project is open source and available for educational and experimental purposes.

## 👨‍💻 Author

**Sergio Nieto**

---

**Note**: This project requires an OpenAI API key to function. API usage will incur costs according to OpenAI's pricing.





