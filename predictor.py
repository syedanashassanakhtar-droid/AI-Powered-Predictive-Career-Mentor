# Predictor stub - replace with real model loading and inference.
import random

def predict_from_text(text):
    '''
    Dummy prediction logic:
     - returns a suggested career path, confidence, and recommended skills.
    Replace this with real ML model inference.
    '''
    careers = ["Data Analyst", "Machine Learning Engineer", "Product Manager", "Software Engineer", "Data Engineer"]
    skills_map = {
        "Data Analyst": ["SQL","Excel","Tableau","Python (pandas)"],
        "Machine Learning Engineer": ["Python","TensorFlow/PyTorch","ML algorithms","Data pipelines"],
        "Product Manager": ["Roadmapping","Communication","Stakeholder management"],
        "Software Engineer": ["Python/Java","APIs","System design"],
        "Data Engineer": ["ETL","Spark","SQL","Cloud (AWS/GCP)"]
    }
    choice = random.choice(careers)
    return {
        "suggested_career": choice,
        "confidence": round(random.uniform(0.55, 0.95),2),
        "recommended_skills": skills_map.get(choice, [])[:4],
        "note": "This is a dummy prediction. Replace predictor.py with your model inference code."
    }
