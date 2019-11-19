from plData.barChartForPL import *

homeWins = cleanDict()
homePoints = cleanDict()
awayWins = cleanDict()
awayPoints = cleanDict()
homeText = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','Home']

def readHomeResults():
    res = open('Results.csv', 'r', encoding='utf-8-sig')
    splitResults = res.read().split('\n')
    splitResults.pop()

    res.close()
    for result in splitResults:
        result = result.split(',')
        hP, aP = evalPoints(result)
        homePoints[result[0]] += hP

        if hP == 3:
            homeWins[result[0]] += 1


def readAwayResults():
    res = open('Results.csv', 'r', encoding='utf-8-sig')
    splitResults = res.read().split('\n')
    splitResults.pop()

    res.close()
    for result in splitResults:
        result = result.split(',')
        hP, aP = evalPoints(result)
        awayPoints[result[3]] += aP

        if aP == 3:
            awayWins[result[3]] += 1

def drawPlots():
    subs = make_subplots(rows = 2, cols = 1)
    homeWinsPlot = go.Scatter(x = ALLTEAMS, y = list(homeWins.values()),name = "Home")
    awayWinsPlot = go.Scatter(x = ALLTEAMS, y = list(awayWins.values()),name = "Away")
    subs.add_trace(homeWinsPlot,row = 1, col = 1)
    subs.add_trace(awayWinsPlot,row = 1, col = 1)

    homePointsPlot = go.Scatter(x = ALLTEAMS, y = list(homePoints.values()),text = homeText, mode = 'lines + text')
    awayPointsPlot = go.Scatter(x = ALLTEAMS, y = list(awayPoints.values()),text = "Away", mode = 'text')
    subs.add_trace(homePointsPlot, row=2, col=1)
    subs.add_trace(awayPointsPlot, row=2, col=1)
    subs.show()

def main():
    readAwayResults()
    readHomeResults()
    drawPlots()
    print(homeWins.values())



if __name__ == '__main__':
    main()




