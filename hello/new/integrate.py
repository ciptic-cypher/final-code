from flask import Flask, request, jsonify
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load models
with open('models/DecisionTree.pkl', 'rb') as f:
    decision_tree_model = pickle.load(f)

with open('models/GradientBoosting.pkl', 'rb') as f:
    gradient_boosting_model = pickle.load(f)

with open('models/LogisticRegression.pkl', 'rb') as f:
    logistic_regression_model = pickle.load(f)

with open('models/RandomForest.pkl', 'rb') as f:
    random_forest_model = pickle.load(f)

with open('models/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Define prediction endpoint for each model
@app.route('/predict/decision_tree', methods=['POST'])
def predict_decision_tree():
    data = request.json
    prediction = decision_tree_model.predict([data['features']])
    return jsonify({'prediction': prediction.tolist()})

@app.route('/predict/gradient_boosting', methods=['POST'])
def predict_gradient_boosting():
    data = request.json
    prediction = gradient_boosting_model.predict([data['features']])
    return jsonify({'prediction': prediction.tolist()})

@app.route('/predict/logistic_regression', methods=['POST'])
def predict_logistic_regression():
    data = request.json
    prediction = logistic_regression_model.predict([data['features']])
    return jsonify({'prediction': prediction.tolist()})

@app.route('/predict/random_forest', methods=['POST'])
def predict_random_forest():
    data = request.json
    prediction = random_forest_model.predict([data['features']])
    return jsonify({'prediction': prediction.tolist()})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)