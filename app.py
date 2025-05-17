from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("stopwords")

app = Flask(__name__, static_folder="static")
CORS(app)

# Load CSV and vectorize
df = pd.read_csv("college_faq.csv")
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["question"])

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "").lower()
    user_vec = vectorizer.transform([user_msg])
    sims = cosine_similarity(user_vec, X)

    best_idx = sims.argmax()
    if sims[0, best_idx] > 0.3:
        reply = df["answer"].iloc[best_idx]
    else:
        reply = "Sorry, I don't know that one."
    return jsonify({"response": reply})

# Rule-based NLTK chatbot
faq_rules = {
    "greet": ["hi", "hello", "hey"],
    "admission": ["admission", "apply", "register", "enroll"],
    "fees": ["fees", "tuition", "cost", "price"],
    "deadline": ["deadline", "last date", "submit"],
    "goodbye": ["bye", "goodbye", "see you"]
}

faq_answers = {
    "greet": "Hi there! How can I help you today?",
    "admission": "You can apply through the college portal with transcripts and SAT/ACT scores.",
    "fees": "The tuition fee is around $15,000 per year.",
    "deadline": "The application deadline is January 15.",
    "goodbye": "Goodbye! Feel free to reach out if you have more questions."
}

def get_intent(user_msg):
    words = word_tokenize(user_msg.lower())
    filtered = [w for w in words if w not in stopwords.words("english")]
    for intent, keywords in faq_rules.items():
        for keyword in keywords:
            if keyword in filtered:
                return faq_answers[intent]
    return "I'm sorry, I didn’t understand that. Can you rephrase?"

@app.route("/chat-nltk", methods=["POST"])
def chat_nltk():
    user_msg = request.json.get("message", "")
    reply = get_intent(user_msg)
    return jsonify({"response": reply})

# Serve frontend
@app.route("/")
def serve_home():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def serve_static_file(path):
    return send_from_directory(app.static_folder, path)
