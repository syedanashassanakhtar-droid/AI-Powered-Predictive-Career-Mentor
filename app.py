from flask import Flask, request, jsonify
from predictor import predict_from_text

app = Flask(__name__)

@app.route("/")
def index():
    return "AI-Powered Predictive Career Mentor - API is running."

@app.route("/predict", methods=["GET","POST"])
def predict():
    if request.method == "GET":
        return jsonify({"message":"Send a POST with JSON {'text': 'resume text'} to get a dummy prediction."})
    data = request.get_json(force=True)
    text = data.get("text","")
    if not text:
        return jsonify({"error":"No 'text' provided"}), 400
    result = predict_from_text(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
