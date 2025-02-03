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

def generate_insight(count, runners, pitch_type):
    prompt = f"""You are a fun baseball commentator explaining strategy to a first-time fan. 

**Situation**:
- Count: {count}
- Runners: {runners}
- Pitch thrown: {pitch_type}

**Task**:
Explain why this pitch was chosen in 1 short sentence. Use a creative analogy from everyday life (e.g., pizza, video games, weather). 

**Rules**:
- No technical terms like "spin rate", "exit velocity", or "WHIP".
- Focus on the pitcher's goal (e.g., strikeout, ground ball).
- Make it relatable and fun!

Example: "The pitcher threw a curveball here — like a rollercoaster suddenly dropping, it fools the batter into swinging too early!"""

    return model.generate_content(prompt).text
