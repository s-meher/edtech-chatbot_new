from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required NLTK data
nltk.download("punkt")
nltk.download("stopwords")

# Flask app
app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

# Load FAQ CSV
df = pd.read_csv("college_faq.csv")
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["question"])

# ML-based chatbot
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

# Rule-based chatbot
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

# Serve index.html
@app.route("/")
def home():
    return render_template("index.html")

# Optional: serve static files
@app.route("/static/<path:path>")
def static_files(path):
    return send_from_directory("static", path)
