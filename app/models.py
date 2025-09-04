"""
models.py - Database setup and table creation
"""
import sqlite3
import os
# This function creates all necessary tables in the database if they don't exist.
def init_db():
    db_path = os.path.join(os.path.dirname(__file__), '../database/health.db')
    # If the file exists but is not a valid database, delete it and recreate
    if os.path.exists(db_path):
        try:
            conn = sqlite3.connect(db_path)
            conn.execute('PRAGMA integrity_check;')
            conn.close()
        except sqlite3.DatabaseError:
            os.remove(db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # Create users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )''')
    # Create questions table
    cursor.execute('''CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        question TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')
    # Create responses table
    cursor.execute('''CREATE TABLE IF NOT EXISTS responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        keyword TEXT,
        advice TEXT
    )''')
    # Create tips table
    cursor.execute('''CREATE TABLE IF NOT EXISTS tips (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tip TEXT
    )''')
    # Create reminders table
    cursor.execute('''CREATE TABLE IF NOT EXISTS reminders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        reminder TEXT,
        date DATE
    )''')
    conn.commit()
    conn.close()
# Run this file directly to initialize the database
if __name__ == "__main__":
    init_db()
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(255), nullable=False)

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(50), unique=True, nullable=False)
    advice = db.Column(db.Text, nullable=False)

class Tip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tip_text = db.Column(db.Text, nullable=False)

class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reminder_text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)