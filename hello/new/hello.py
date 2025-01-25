import pandas as pd
import numpy as np
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

# Load data
data_fake = pd.read_csv('Downloads/Fake.csv')
data_true = pd.read_csv('Downloads/True.csv')

# Add class labels
data_fake["class"] = 0
data_true["class"] = 1

# Remove last 10 rows for manual testing
data_fake_manual_testing = data_fake.tail(10)
data_fake = data_fake.iloc[:-10]
data_true_manual_testing = data_true.tail(10)
data_true = data_true.iloc[:-10]

# Combine datasets
data = pd.concat([data_fake, data_true], axis=0)
data = data.sample(frac=1).reset_index(drop=True)

# Drop unnecessary columns
data = data.drop(['title', 'subject', 'date'], axis=1)

# Text preprocessing function
def wordopt(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(rf'[{string.punctuation}]', '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text

data['text'] = data['text'].apply(wordopt)

# Split data into training and testing sets
x = data['text']
y = data['class']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

# Vectorization
vectorization = TfidfVectorizer()
xv_train = vectorization.fit_transform(x_train)
xv_test = vectorization.transform(x_test)

# Models and training
models = {
    "LogisticRegression": LogisticRegression(),
    "DecisionTree": DecisionTreeClassifier(),
    "GradientBoosting": GradientBoostingClassifier(random_state=0),
    "RandomForest": RandomForestClassifier(random_state=0)
}

# Directory to save models
os.makedirs("models", exist_ok=True)

for model_name, model in models.items():
    model.fit(xv_train, y_train)
    predictions = model.predict(xv_test)
    print(f"\n{model_name} Classification Report:\n")
    print(classification_report(y_test, predictions))
    joblib.dump(model, f"models/{model_name}.pkl")

# Save vectorizer
joblib.dump(vectorization, "models/vectorizer.pkl")

print("\nAll models and vectorizer have been saved in the 'models' directory.")
