import os
import sqlite3
# Gemini API integration
import google.genai as genai

# Set Gemini API key (recommended: set as environment variable GEMINI_API_KEY)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyBAPPZrsuFvN4OXgxk1nh7klUxkv8B0GDo")
client = genai.Client(api_key=GEMINI_API_KEY)

def get_response(user_input):
    """
    Uses Gemini API to generate concise health advice.
    Falls back to keyword matching if Gemini API fails.
    """
    try:
        # Construct a prompt that encourages brief, focused health advice
        prompt = f"""As a health advisor, provide a brief, professional response about: {user_input}
        Requirements:
        - Keep it under 3 sentences
        - Focus on practical health advice
        - Include a clear recommendation
        - Be direct and professional
        - If it's a serious condition, recommend consulting a healthcare provider
        """
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        # Fallback to keyword matching if Gemini API fails
        db_path = os.path.join(os.path.dirname(__file__), '../database/health.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        user_input_lower = user_input.lower()
        cursor.execute("SELECT advice FROM responses WHERE ? LIKE '%' || keyword || '%'", (user_input_lower,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return result[0]
        else:
            return "Sorry, I couldn't find advice for your query. Please consult a healthcare professional if needed."