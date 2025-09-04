"""
Smart Health Advisor - Main Flask App
"""
from flask import Flask
from flask_cors import CORS
from app.routes import main
import os

# Set template folder to app/templates
template_dir = os.path.join(os.path.dirname(__file__), 'app', 'templates')
app = Flask(__name__, template_folder=template_dir)
CORS(app)  # Enable CORS for all routes
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)
