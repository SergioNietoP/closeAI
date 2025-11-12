from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai
import os
import json

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')


@app.route('/')
def index():
    """Main page with project overview"""
    return render_template('index.html')


@app.route('/interview-evaluator')
def interview_evaluator():
    """Interview evaluation tool page"""
    return render_template('interview_evaluator.html')


@app.route('/question-generator')
def question_generator():
    """Question generator tool page"""
    return render_template('question_generator.html')


@app.route('/text-analyzer')
def text_analyzer():
    """Text analysis tool page"""
    return render_template('text_analyzer.html')


@app.route('/chat')
def chat():
    """Chat interface page"""
    return render_template('chat.html')


@app.route('/api/evaluate-answer', methods=['POST'])
def evaluate_answer():
    """API endpoint to evaluate interview answers"""
    try:
        data = request.json
        question = data.get('question', '')
        answer = data.get('answer', '')
        
        if not question or not answer:
            return jsonify({'error': 'Question and answer are required'}), 400
        
        system_instruction = (
            f"You are the best personality test evaluator. You are going to receive an answer "
            f"from a candidate that is applying for a job to this question: '{question}'. "
            f"I need you to give scores based on these metrics: Specificity, Relevance, "
            f"Problem-Solving, Initiative, Outcome, Self-Reflection, Creativity, Communication. "
            f"Also, give me a short explanation of your evaluation with pros and cons. "
            f"Give an answer in JSON format where each field is a metric (score from 1-10), "
            f"and also add average score and the explanation fields."
        )
        
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.8,
            max_tokens=2000,
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": answer}
            ]
        )
        
        result = completion.choices[0].message.content
        
        # Try to parse as JSON, if fails return as text
        try:
            result_json = json.loads(result)
            return jsonify({'success': True, 'evaluation': result_json})
        except json.JSONDecodeError:
            return jsonify({'success': True, 'evaluation': {'raw': result}})
            
    except Exception as e:
        # Log the actual error but don't expose details to users
        app.logger.error(f'Error evaluating answer: {str(e)}')
        return jsonify({'error': 'An error occurred while processing your request. Please try again.'}), 500


@app.route('/api/generate-questions', methods=['POST'])
def generate_questions():
    """API endpoint to generate questions for topics"""
    try:
        data = request.json
        topics = data.get('topics', [])
        
        if not topics:
            return jsonify({'error': 'Topics array is required'}), 400
        
        system_instruction = (
            "You are the best question generator, you know about everything. "
            "You are going to receive an array of assessable objects. For each assessable "
            "you will have the title and the description. Based on that info I want you to "
            "develop questions to evaluate the knowledge of users in this topic. For each "
            "assessable, you have to choose 4 topics. Each topic will have 5 questions "
            "related to this topic (this is very important) in total 20 questions. "
            "Give the answer with this structure: assessable_title: { topic_title1: "
            "{ question_1, question_2, ..., question_5 }, topic_title2: {}}. "
            "Fill each variable of the output with its corresponding value. Return valid JSON."
        )
        
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.8,
            max_tokens=3000,
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": json.dumps(topics)}
            ]
        )
        
        result = completion.choices[0].message.content
        
        return jsonify({'success': True, 'questions': result})
            
    except Exception as e:
        # Log the actual error but don't expose details to users
        app.logger.error(f'Error generating questions: {str(e)}')
        return jsonify({'error': 'An error occurred while processing your request. Please try again.'}), 500


@app.route('/api/analyze-text', methods=['POST'])
def analyze_text():
    """API endpoint to analyze text"""
    try:
        data = request.json
        text = data.get('text', '')
        analysis_type = data.get('type', 'general')
        
        if not text:
            return jsonify({'error': 'Text is required'}), 400
        
        prompts = {
            'general': 'Analyze this text and provide insights about its content, tone, and structure.',
            'sentiment': 'Analyze the sentiment of this text. Is it positive, negative, or neutral? Explain why.',
            'grammar': 'Review this text for grammar, spelling, and punctuation errors. Provide corrections and suggestions.',
            'summary': 'Provide a concise summary of this text, highlighting the main points.'
        }
        
        prompt = prompts.get(analysis_type, prompts['general'])
        
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.7,
            max_tokens=1500,
            messages=[
                {"role": "system", "content": f"{prompt} Provide your response in a clear, structured format."},
                {"role": "user", "content": text}
            ]
        )
        
        result = completion.choices[0].message.content
        
        return jsonify({'success': True, 'analysis': result})
            
    except Exception as e:
        # Log the actual error but don't expose details to users
        app.logger.error(f'Error analyzing text: {str(e)}')
        return jsonify({'error': 'An error occurred while processing your request. Please try again.'}), 500


@app.route('/api/chat', methods=['POST'])
def chat_api():
    """API endpoint for chat functionality"""
    try:
        data = request.json
        message = data.get('message', '')
        conversation_history = data.get('history', [])
        
        if not message:
            return jsonify({'error': 'Message is required'}), 400
        
        messages = [
            {"role": "system", "content": "You are a helpful AI assistant with expertise in various topics. Provide clear, informative, and friendly responses."}
        ]
        
        # Add conversation history
        messages.extend(conversation_history)
        
        # Add current message
        messages.append({"role": "user", "content": message})
        
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.8,
            max_tokens=1500,
            messages=messages
        )
        
        result = completion.choices[0].message.content
        
        return jsonify({'success': True, 'response': result})
            
    except Exception as e:
        # Log the actual error but don't expose details to users
        app.logger.error(f'Error in chat: {str(e)}')
        return jsonify({'error': 'An error occurred while processing your request. Please try again.'}), 500


@app.errorhandler(404)
def not_found(e):
    """404 error handler"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    """500 error handler"""
    return render_template('500.html'), 500


if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True') == 'True'
    
    app.run(host=host, port=port, debug=debug)
