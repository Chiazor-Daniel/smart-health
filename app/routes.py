from flask import Blueprint, request, jsonify, render_template
from app.chatbot import get_response
import sqlite3
import os

# Define the main blueprint for routes
main = Blueprint('main', __name__)

# Home page route
@main.route('/')
def index():
    return render_template('index.html')

# Chat API endpoint
@main.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No message provided'}), 400
    response = get_response(user_input)
    return jsonify({'response': response})

# Endpoint to get a random daily health tip
@main.route('/tip')
def tip():
    db_path = os.path.join(os.path.dirname(__file__), '../database/health.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT tip FROM tips ORDER BY RANDOM() LIMIT 1')
    result = cursor.fetchone()
    conn.close()
    return jsonify({'tip': result[0] if result else 'Stay healthy!'})