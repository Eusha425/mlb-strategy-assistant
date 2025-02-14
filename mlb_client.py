import requests 
import date


def get_game_id():

    today = date.get_current_date()
    # print(today)
    #today = "2021-08-08" # a testing date

    # retrieve the request from mlb api in json format
    response = requests.get(f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={today}").json()
    #print(response)

    #print(req["totalGames"])

    #print(req["dates"][0]['games'][0]['gamePk'])

    # check if there are any games for the current date
    if response["totalGames"] == 0:
        #print("No game")
        return 0       
    else:
        #print(req["games"])

        # get the game primary key from the json response
        gameId = response["dates"][0]['games'][0]['gamePk']

        return gameId
        #print(gameId)

def get_game_data():
    game_id = get_game_id()
    if game_id == 0:
        return 0
    else:
        # Retrieve detailed live game data
        game_data = requests.get(f"https://statsapi.mlb.com/api/v1.1/game/{game_id}/feed/live").json()
        # print(game_data)
        
        # Try to extract additional info such as inning and score
        try:
            linescore = game_data["liveData"]["linescore"]
            inning = linescore.get("currentInning", "N/A")
            home_score = linescore["teams"]["home"]["runs"]
            away_score = linescore["teams"]["away"]["runs"]
        except Exception:
            inning = "N/A"
            home_score = 0
            away_score = 0
        
        # Store additional game info in a dedicated key
        game_data["game_info"] = {
            "inning": inning,
            "home_score": home_score,
            "away_score": away_score
        }
        return game_data