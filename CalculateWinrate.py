import MatchInformation
import Constants

def calculateWinrate(matchInfoList):
    wins = 0
    numGames = float(len(matchInfoList))
    
    for matchInfo in matchInfoList:
        # print(matchInfo.win)
        if matchInfo.win == True:
            # print("match won")
            wins += 1
        else:
            pass
            # print("match lost")
    
    winrate = (wins / numGames) * 100
    
    return winrate