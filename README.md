# EdTech Chatbot

An interactive educational chatbot built with Flask and JavaScript. This project demonstrates both rule-based and predictive chatbot models to help students get answers and engage in academic conversations.

## Features

- Rule-based chatbot using NLTK
- Predictive chatbot using Keras Sequential model
- Clean web interface (HTML, CSS, JS)
- Flask backend for chatbot logic
- Easy to modify and expand

## Project Structure
edtech-chatbot_new/

├── app.py              # Flask backend logic

├── index.html          # Frontend interface

├── script.js           # Handles user interaction

├── style.css          

## Installation

### Requirements

- Python 3.x
- pip

### Steps

1. Clone this repo:
   ```bash
   git clone https://github.com/s-meher/edtech-chatbot_new.git
   cd edtech-chatbot_new
2. Install the required libraries:
   pip install -r requirements.txt
3. Run the app:
   python app.py


### How it Works
You type a message in the browser.

JavaScript sends the message to the Flask backend (app.py).

The backend responds using rule-based or ML model logic.

The message and response are shown in the chat window.



