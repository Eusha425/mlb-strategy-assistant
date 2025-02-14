import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure API key 
key = GEMINI_API_KEY  
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-pro')

def generate_insight(count, runners, pitch_type, extra_context=""):
    prompt = f"""You are a fun baseball commentator explaining strategy to a first-time fan.

**Situation**:
- Count: {count}
- Runners: {runners}
- Pitch thrown: {pitch_type}
{extra_context}

**Task**:
Explain why this pitch was chosen in 1 short sentence using a creative analogy from everyday life (e.g., pizza, video games, weather)."""
    return model.generate_content(prompt).text