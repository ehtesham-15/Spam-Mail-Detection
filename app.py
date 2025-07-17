from flask import Flask, request, jsonify, render_template
import joblib
# Load model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    emails = data.get("emails", [])

    features = vectorizer.transform(emails)
    predictions = model.predict(features)

    results = [{"email": email, "result": "Not SPAM" if pred == 1 else "SPAM"} for email, pred in zip(emails, predictions)]

    return jsonify(results)

if __name__ == '_main_':
    app.run(debug=True)