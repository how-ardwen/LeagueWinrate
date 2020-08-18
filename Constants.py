import requests
import json

token = "RGAPI-dbe3a770-2a95-417c-b028-a629f8a15052"
accountIDInput = input("Enter Summoner Name: ")

def getAccountID(accountIDName):
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + accountIDName.replace(" ", "%20")

    queryParams = {
        "api_key": token
    }

    response = requests.get(url, params=queryParams)

    if response.status_code == 200:
        responseData = json.loads(response.text)
        accountID = responseData["accountId"]
        return accountID
    else:
        return 0

if getAccountID(accountIDInput) == 0:
    print("Unknown Summoner Name...")

accountID = getAccountID(accountIDInput)