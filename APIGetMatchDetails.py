import requests
import json
import Constants
import MatchInformation

def getAllMatches(gameList, champID):
    matches = []
    for i in range(len(gameList)):
        print("Getting game", i, "out of", len(gameList))
        matchInfo = getMatchDetails(gameList[i], champID)
        if matchInfo != -1:
            matches.append(matchInfo)

    return matches

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

        winBoolean = determineWin(participants, champID)

        match = MatchInformation.MatchInformation(gameID, champID, gameDuration, winBoolean)
        
        return match
    
    else:
        print(response.status_code)
        return -1

# def getPlayerTeamID(players, champID):
#     for p in players:
#         if p["championId"] == champID:
#             return p["teamId"]
#     return "Error: champ not found"

# def checkWin(teams, teamID):
#     for t in teams:
#         if t["teamId"] == teamID:
#             if t["win"] == "Win":
#                 return True
#             else:
#                 return False

def determineWin(participants, champID):
    for p in participants:
        if p["championId"] == int(champID):
            # print(type(p["stats"]["win"]))
            if p["stats"]["win"] == True:
                return True
            else:
                return False
        else:
            # print(p["championId"], "is not my champion")
            pass
    print("Could not find player champion")
    return -1