<<<<<<< HEAD
import requests
import json

token = "YOUR_TOKEN_HERE"
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
=======
accountID = insert
token = insert
>>>>>>> 383b34fc1db8c8a3370904ff3e0612f29d6e80cd
