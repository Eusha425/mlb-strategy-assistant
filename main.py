import google.generativeai as genai
import os
from datetime import datetime
import requests

# Configure API key 
key = "AIzaSyCsuoQYxrzc8s4FQGkOuWMdIBowynJX1pA"  # Hardcoded for testing (remove later)
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-pro')

def get_live_game_id():
    """Fetch today's MLB game ID."""
    today = datetime.today().strftime('%Y-%m-%d')
    try:
        schedule = requests.get(
            f"https://statsapi.mlb.com/api/v1/schedule?date={today}",
            timeout=5
        ).json()
        if schedule.get("dates"):
            return schedule["dates"][0]["games"][0]["gamePk"], "demo"  # First game of day
        return None, None
    except Exception as e:
        print(f"Schedule error: {str(e)}")
        return None, None

def generate_insight(pitch_type, count, runners):
    """Generate pitch explanation."""
    prompt = f"""Explain this baseball pitch to a casual fan:
- Count: {count}
- Runners: {runners}
- Pitch type: {pitch_type}
Use 1 fun sentence!"""
    try:
        return model.generate_content(prompt).text
    except Exception as e:
        return f"Insight error: {str(e)}"

def main():
    game_id, status = get_live_game_id()
    game_id = game_id or "716757"  # Fallback to test ID if needed
    
    try:
        game_data = requests.get(
            f"https://statsapi.mlb.com/api/v1.1/game/{game_id}/feed/live"
        ).json()
        
        # CORRECTED: Get linescore from liveData (not plays)
        linescore = game_data.get("liveData", {}).get("linescore", {})
        if not linescore:
            print("No linescore data available")
            return

        # Get count from linescore
        count = f"{linescore.get('balls', 0)}-{linescore.get('strikes', 0)}"
        
        # Get latest pitch data
        plays = game_data.get("liveData", {}).get("plays", {})
        if plays.get("currentPlay"):
            latest_pitch = plays["currentPlay"]["playEvents"][-1]
            pitch_type = latest_pitch["details"]["type"]["description"]
        else:
            pitch_type = "Unknown pitch"

        # Get runners
        offense = linescore.get("offense", {})
        runners = offense.get("situation", {}).get("description", "no runners")

        print("\n⚾ Live Analysis:")
        print(generate_insight(pitch_type, count, runners))
        
    except Exception as e:
        print(f"Fatal error: {str(e)}")

if __name__ == "__main__":
    main()