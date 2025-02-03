import mlb_client
import gemini_client

data = mlb_client.get_game_data()

if data == 0:
    print("No Game for the current date")
else:
    # Ensure data has the required keys before accessing them
    if "liveData" in data and "plays" in data["liveData"] and "currentPlay" in data["liveData"]["plays"]:
        latest_pitch = data["liveData"]["plays"]["currentPlay"]["playEvents"][-1]
        pitch_type = latest_pitch["details"]["type"]["description"]
        balls = data["liveData"]["linescore"]["balls"]
        strikes = data["liveData"]["linescore"]["strikes"]
        count = f"{balls}-{strikes}"
        
        # Check if offense situation exists before accessing it
        runners = data["liveData"]["linescore"]["offense"].get("situation", {}).get("description", "No runners on base")

        response = gemini_client.generate_insight(count, runners, pitch_type)

        print(response)
        
    else:
        print("Error: Game data missing required fields")


