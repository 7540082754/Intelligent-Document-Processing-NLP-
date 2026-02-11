from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

def train():
    X = [
        "invoice number total amount gst",
        "skills experience education resume"
    ]
    y = ["invoice", "resume"]

    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", LogisticRegression())
    ])

    model.fit(X, y)
    joblib.dump(model, "models/doc_classifier.pkl")

def predict(text):
    model = joblib.load("models/doc_classifier.pkl")
    return model.predict([text])[0]
