import APIGetMatchDetails
import MatchInformation
import Constants
from enum import Enum

class GameLength(Enum):
    SHORT = 20
    MEDIUM = 30
    LONG = 31

def filterMatchesByLength(matchInfoList, length):
    filteredMatches = []
    for matchInfo in matchInfoList:
        matchMinutes = matchInfo.durationSec / 60.0
        if matchMinutes <= GameLength.SHORT.value and length == GameLength.SHORT:
            filteredMatches.append(matchInfo)
        elif matchMinutes <= GameLength.MEDIUM.value and matchMinutes > GameLength.SHORT.value and length == GameLength.MEDIUM:
            filteredMatches.append(matchInfo)
        elif matchMinutes > GameLength.MEDIUM.value and length == GameLength.LONG:
            filteredMatches.append(matchInfo)
    
    return filteredMatches

# tempGameList = [3490451817, 3490345969, 3485693091, 3460872596, 3459630014]

# matchArray = APIGetMatchDetails.getAllMatches(tempGameList, 69)

# testMatchBucket = filterMatchesByLength(matchArray, GameLength.MEDIUM)

# for test in testMatchBucket:
#     print(test.durationSec)
#     print(test.win)