# Smart Health Advisor

## Project Overview
The Smart Health Advisor is a web-based health chatbot designed to provide users with health advice based on their symptoms. The chatbot utilizes a Flask backend and an SQLite database to store and retrieve health-related information.

## Features
- Interactive chatbot interface for user queries.
- Keyword-based response generation from a pre-filled database.
- Simple and user-friendly design.

## Project Structure
```
Smart-Health-Advisor
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── chatbot.py
│   └── static
│       └── style.css
│   └── templates
│       ├── index.html
│       └── chat.html
├── database
│   └── health.db
├── requirements.txt
├── config.py
├── README.md
└── run.py
```

# Smart Health Advisor

A beginner-friendly web-based health chatbot built with Python Flask and SQLite.

## Features
- Chatbot answers health questions using keyword matching
- Daily health tips section
- WhatsApp-style chat bubbles
- Easy to run locally

## Setup Instructions

1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Initialize the database**
   ```bash
   python app/models.py
   python database/init_sample_data.py
   ```
4. **Run the app**
   ```bash
   flask run
   ```
5. **Open in browser**
   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

## File Structure
- `app.py` - Main Flask app
- `app/models.py` - Database setup
- `app/chatbot.py` - Chatbot logic
- `app/routes.py` - API endpoints
- `app/templates/index.html` - Frontend UI
- `app/static/style.css` - Extra styling
- `database/health.db` - SQLite database

## Sample Data
- Responses for keywords: headache, fever, malaria, etc.
- Daily health tips

## Notes
- All code is commented for beginners
- You can extend the chatbot by adding more keywords and advice in the database

## Troubleshooting
- If you get database errors, make sure you have run both `python app/models.py` and `python database/init_sample_data.py` to create and fill the database.

## How it works
- The chatbot uses simple keyword matching to answer health questions.
- Health tips are shown randomly from the database each time you load the page.# smart-health
# smart-health
