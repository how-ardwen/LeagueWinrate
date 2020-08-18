#This file is going to be for pulling data from the Riot API
import json
import requests
import Constants

def getChampID():
    championName = input("Champion Name: ")
    targetUrl = "http://ddragon.leagueoflegends.com/cdn/10.16.1/data/en_US/champion.json"
    response = requests.get(targetUrl)

    if response.status_code == 200:
        responseData = json.loads(response.text)

        champions = responseData["data"]
        champData = champions[championName]
        idNum = champData["key"]    
        return idNum

def getListOfGames(champID):
    gameList = []
    baseURL = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + Constants.accountID
    
    queryParams = {
        "api_key": Constants.token,
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