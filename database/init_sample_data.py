"""
Script to pre-fill health.db with sample responses and tips
"""
import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'health.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Sample responses
responses = [
    ('headache', 'For headaches, drink water, rest, and avoid screen time. If severe, consult a doctor.'),
    ('fever', 'For fever, stay hydrated and rest. If high or persistent, seek medical attention.'),
    ('malaria', 'Malaria requires prompt medical treatment. Use mosquito nets and consult a doctor.'),
    ('cough', 'For cough, drink warm fluids and rest. If persistent, see a healthcare provider.'),
    ('cold', 'For cold, rest and drink fluids. If symptoms worsen, consult a doctor.')
]
cursor.executemany('INSERT INTO responses (keyword, advice) VALUES (?, ?)', responses)

# Sample health tips
tips = [
    ('Drink plenty of water every day.'),
    ('Wash your hands regularly.'),
    ('Get enough sleep for better health.'),
    ('Exercise regularly to stay fit.'),
    ('Eat a balanced diet rich in fruits and vegetables.')
]
cursor.executemany('INSERT INTO tips (tip) VALUES (?)', [(t,) for t in tips])

conn.commit()
conn.close()
