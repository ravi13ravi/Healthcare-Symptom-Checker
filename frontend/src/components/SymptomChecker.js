import React, { useState } from 'react';
import axios from 'axios';
import './SymptomChecker.css';

const SymptomChecker = () => {
  const [symptoms, setSymptoms] = useState('');
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await axios.post('http://localhost:5000/api/analyze', {
        symptoms
      });
      setAnalysis(response.data.analysis);
    } catch (err) {
      setError('An error occurred while analyzing symptoms. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="symptom-checker">
      <div className="disclaimer">
        <h2>
          <span role="img" aria-label="healthcare">⚕️</span>
          Healthcare Symptom Checker
        </h2>
        <p className="disclaimer-text">
          <span role="img" aria-label="warning">⚠️</span> IMPORTANT: This tool is for educational purposes only. 
          This is not medical advice. Please consult a qualified healthcare 
          professional for actual medical advice, diagnosis, or treatment.
        </p>
      </div>

      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <label htmlFor="symptoms">
            <span role="img" aria-label="clipboard">📋</span> Describe your symptoms:
          </label>
          <textarea
            id="symptoms"
            value={symptoms}
            onChange={(e) => setSymptoms(e.target.value)}
            placeholder="Please provide detailed information about your symptoms, including:
- What symptoms are you experiencing?
- When did they start?
- Are they constant or do they come and go?
- Does anything make them better or worse?"
            required
          />
        </div>
        <button type="submit" disabled={loading}>
          {loading ? (
            <>Analyzing Symptoms</>
          ) : (
            <>
              <span role="img" aria-label="analyze">🔍</span> Analyze Symptoms
            </>
          )}
        </button>
      </form>

      {error && (
        <div className="error">
          <span role="img" aria-label="error">⚠️</span> {error}
        </div>
      )}

      {analysis && (
        <div className="analysis">
          <h3>
            <span role="img" aria-label="results">📊</span> Analysis Results
          </h3>
          <div className="analysis-content">
            {analysis}
          </div>
        </div>
      )}
    </div>
  );
};

export default SymptomChecker;