import APIGetGameIDs
import APIGetMatchDetails
import SplitTimeBucket
import CalculateWinrate
import MatchInformation
import Constants
from pprint import pprint


def getRelativeWinrate():
    champID = APIGetGameIDs.getChampID()
    gameIDList = APIGetGameIDs.getListOfGames(champID)
    matchDetailsList = APIGetMatchDetails.getAllMatches(gameIDList, champID)

    shortBucket = SplitTimeBucket.filterMatchesByLength(matchDetailsList, SplitTimeBucket.GameLength.SHORT)
    medBucket = SplitTimeBucket.filterMatchesByLength(matchDetailsList, SplitTimeBucket.GameLength.MEDIUM)
    longBucket = SplitTimeBucket.filterMatchesByLength(matchDetailsList, SplitTimeBucket.GameLength.LONG)

    shortWR = CalculateWinrate.calculateWinrate(shortBucket)
    medWR = CalculateWinrate.calculateWinrate(medBucket)
    longWR = CalculateWinrate.calculateWinrate(longBucket)
    overallWR = CalculateWinrate.calculateWinrate(matchDetailsList)

    print("Overall winrate:", overallWR)
    print("Short winrate:", shortWR)
    print("Medium winrate:", medWR)
    print("Long winrate:", longWR)

getRelativeWinrate()