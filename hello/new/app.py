from flask import Flask, request, jsonify
import pandas as pd
import joblib
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier

# Initialize Flask app
app = Flask(__name__)

# Load models and vectorizer
LR = joblib.load("models/logistic_regression.pkl")  # Replace with your model paths
DT = joblib.load("models/decision_tree.pkl")
GB = joblib.load("models/gradient_boosting.pkl")
RF = joblib.load("models/random_forest.pkl")
vectorization = joblib.load("models/vectorizer.pkl")

# Preprocessing function
def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W", " ", text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

# Output label mapping
def output_label(n):
    return "Fake News" if n == 0 else "Not Fake News"

# Define the prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the news article from the request
        data = request.get_json()
        news = data.get('news', '')

        if not news:
            return jsonify({"error": "No news content provided"}), 400

        # Preprocess the input
        processed_text = wordopt(news)
        vectorized_text = vectorization.transform([processed_text])

        # Get predictions from all models
        pred_LR = output_label(LR.predict(vectorized_text)[0])
        pred_DT = output_label(DT.predict(vectorized_text)[0])
        pred_GB = output_label(GB.predict(vectorized_text)[0])
        pred_RF = output_label(RF.predict(vectorized_text)[0])

        # Return the predictions as a JSON response
        return jsonify({
            "Logistic Regression": pred_LR,
            "Decision Tree": pred_DT,
            "Gradient Boosting": pred_GB,
            "Random Forest": pred_RF
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
