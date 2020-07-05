#This file is going to be for pulling data from the Riot API
import json
import requests

accountID = "C8o8Ir2OGDC_qJMfhCE8etWQ9KnbkAoJxBQXrDVxoZX-8xY"
token = "RGAPI-cde122c5-278d-4e30-a34e-f63024bf365f"

def getChampID():
    championName = input("Champion Name: ")
    targetUrl = "http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json"
    response = requests.get(targetUrl)

    if response.status_code == 200:
        responseData = json.loads(response.text)

        champions = responseData["data"]
        champData = champions[championName]
        idNum = champData["key"]    
        return idNum

def getListOfGames(champID):
    gameList = []
    baseURL = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountID
    
    queryParams = {
        "api_key": token,
        "champion": champID
    }

    response = requests.get(baseURL, params=queryParams)

    if response.status_code == 200:
        responseData = json.loads(response.text)
        matches = responseData["matches"]

        for match in matches:
            gameID = match["gameId"]
            gameList.append(gameID)

    return gameList

print(getListOfGames(getChampID()))