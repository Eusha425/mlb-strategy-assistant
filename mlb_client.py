import requests 
import date


def get_game_id():

    today = date.get_current_date()
    # print(today)
    #today = "2024-10-13" # a testing date

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

    id = get_game_id()
    if id == 0:
        return 0
    else:
        # retrieve the gameplay data for the given id
        game_data = requests.get(f"https://statsapi.mlb.com/api/v1.1/game/{id}/feed/live").json()

        #print(game_data)

        return game_data