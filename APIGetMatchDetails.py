import requests
import json
import Constants
import MatchInformation

def getMatchDetails(gameID, champID):
    baseURL = "https://na1.api.riotgames.com/lol/match/v4/matches/" + str(gameID)

    queryParams = {
        "api_key": Constants.token
    }

    response = requests.get(baseURL, params=queryParams)

    if response.status_code == 200:
        responseData = json.loads(response.text)
        
        gameDuration = responseData["gameDuration"]
        participants = responseData["participants"]
        teams = responseData["teams"]

        teamID = getPlayerTeamID(participants, champID)
        winBoolean = checkWin(teams, teamID)

        match = MatchInformation.MatchInformation(gameID, champID, gameDuration, winBoolean)
        return match

def getPlayerTeamID(players, champID):
    for p in players:
        if p["championId"] == champID:
            return p["teamId"]
    return "Error: champ not found"

def checkWin(teams, teamID):
    for t in teams:
        if t["teamId"] == teamID:
            if t["win"] == "Win":
                return True
            else:
                return False

match = getMatchDetails(3459630014, 69)
print(match.durationSec)
print(match.win)