# AI_Powered_Predictive_Career_Mentor

An AI-powered predictive career mentor project scaffold. Includes a minimal Flask API, example model placeholder, and instructions to run locally.

## What's included
- `app.py` - minimal Flask app with endpoints to get a dummy prediction
- `model_placeholder.txt` - placeholder explaining where to put your trained model
- `requirements.txt` - Python dependencies
- `predictor.py` - prediction logic stub
- `utils.py` - helper functions
- `sample_data/resume_example.txt` - example resume text

## Quick start
1. Create a virtualenv: `python -m venv venv` 
2. Activate it and install: `pip install -r requirements.txt`
3. Run: `python app.py`
4. Open `http://127.0.0.1:5000/predict` (GET) or POST to `/predict` with JSON `{"text": "your resume text"}`.

Replace `model_placeholder.txt` with a real trained model (e.g., `model.pkl`) and update `predictor.py` accordingly.
