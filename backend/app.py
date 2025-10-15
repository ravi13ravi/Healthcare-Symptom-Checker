from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv
import sqlite3
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

def init_db():
    conn = sqlite3.connect('queries.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS queries
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  symptoms TEXT NOT NULL,
                  analysis TEXT NOT NULL,
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

# Initialize database
init_db()

def get_medical_analysis(symptoms):
    try:
        if not openai.api_key:
            raise ValueError("OpenAI API key is not configured. Please check your .env file.")
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """You are a medical information assistant providing educational guidance only. 
                Always include this disclaimer: 'IMPORTANT: This is for educational purposes only. This is not medical advice. 
                Please consult a qualified healthcare professional for actual medical advice, diagnosis, or treatment.'"""},
                {"role": "user", "content": f"Based on these symptoms, suggest possible conditions and next steps (for educational purposes only): {symptoms}"}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message['content']
    except openai.error.RateLimitError:
        return "Error: OpenAI API rate limit exceeded. Please try again later or check your API quota."
    except openai.error.AuthenticationError:
        return "Error: Invalid OpenAI API key. Please check your API key configuration."
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/api/analyze', methods=['POST'])
def analyze_symptoms():
    if not request.json or 'symptoms' not in request.json:
        return jsonify({'error': 'No symptoms provided'}), 400

    symptoms = request.json['symptoms']
    
    # Get analysis from OpenAI
    analysis = get_medical_analysis(symptoms)
    
    # Store in database
    try:
        conn = sqlite3.connect('queries.db')
        c = conn.cursor()
        c.execute('INSERT INTO queries (symptoms, analysis) VALUES (?, ?)',
                 (symptoms, analysis))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")

    return jsonify({
        'symptoms': symptoms,
        'analysis': analysis
    })

@app.route('/api/history', methods=['GET'])
def get_history():
    try:
        conn = sqlite3.connect('queries.db')
        c = conn.cursor()
        c.execute('SELECT * FROM queries ORDER BY timestamp DESC LIMIT 10')
        queries = c.fetchall()
        conn.close()
        
        return jsonify([{
            'id': q[0],
            'symptoms': q[1],
            'analysis': q[2],
            'timestamp': q[3]
        } for q in queries])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)