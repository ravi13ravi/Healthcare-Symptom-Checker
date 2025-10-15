# Healthcare Symptom Checker

A web application that provides educational information about possible health conditions based on user-reported symptoms. This application uses OpenAI's GPT model to analyze symptoms and provide general information and recommendations.

## ⚠️ Important Disclaimer

**This application is for EDUCATIONAL PURPOSES ONLY.**
- This is NOT a substitute for professional medical advice, diagnosis, or treatment.
- Always seek the advice of your physician or other qualified health provider.
- Never disregard professional medical advice or delay seeking it because of something you have read on this application.
- If you think you may have a medical emergency, call your doctor or emergency services immediately.

## Features

- Input interface for describing symptoms
- AI-powered analysis of symptoms
- Educational information about possible conditions
- Recommended next steps (for educational purposes)
- Query history tracking
- Clear medical disclaimers

## Technical Stack

- Backend: Python Flask
- Frontend: React
- Database: SQLite
- AI: OpenAI GPT-3.5

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a .env file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

## Running the Application

1. Start the backend server (from the backend directory):
   ```bash
   python app.py
   ```

2. Start the frontend development server (from the frontend directory):
   ```bash
   npm start
   ```

3. Access the application at `http://localhost:3000`

## API Endpoints

- `POST /api/analyze`
  - Analyzes symptoms and returns possible conditions
  - Request body: `{ "symptoms": "description of symptoms" }`

- `GET /api/history`
  - Returns the last 10 queries and their results

## Security and Privacy

- This application does not provide medical advice
- No personal health information should be stored
- All queries are anonymized
- Data is stored locally in SQLite database

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.