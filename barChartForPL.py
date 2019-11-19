import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd
ALLTEAMS = ['Arsenal', 'Bournemouth', 'Brighton', 'Burnley', 'Cardiff City', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Huddersfield Town', 'Leicester City', 'Liverpool', 'Man City', 'Man Utd', 'Newcastle United', 'Southampton', 'Spurs', 'Watford', 'West Ham', 'Wolves']
TOP6 = ['Arsenal','Chelsea','Liverpool','Man City','Man Utd','Spurs']
selectedTeams = []
from collections import OrderedDict



def evalPoints(result):
    h = int(result[1])
    a = int(result[2])
    if h > a:
        return 3, 0
    elif h < a:
        return 0, 3
    else:
        return 1, 1


def cleanDict():
    return OrderedDict((team, 0) for team in ALLTEAMS)


def readResults():
    pointsTable = OrderedDict((team, cleanDict()) for team in ALLTEAMS)

    res = open('Results.csv', 'r', encoding='utf-8-sig')
    splitResults = res.read().split('\n')
    splitResults.pop()
    a = 0

    for result in splitResults:
        result = result.split(',')
        homePoints, awayPoints = evalPoints(result)
        pointsTable[result[0]][result[3]] += homePoints

        pointsTable[result[3]][result[0]] += awayPoints
        if pointsTable['Arsenal']['Arsenal'] > 0:
            print(result)

    return pointsTable


def writeToFile(pointsTable):
    f = open('AllPoints.csv', 'w')
    f.write("Teams ,")
    for team in ALLTEAMS:
        f.write(team + ",")

    for k in pointsTable:
        f.write('\n')
        f.write(k + ',')
        for p in pointsTable[k]:
            f.write(str(pointsTable[k][p]) + ',')

    f.close()


def sortData(teamName):
    f = open('AllPoints.csv', 'r')

    tRows = f.read().split('\n')

    splitRows = [r.split(',') for r in tRows]
    splitRows[0].pop(0)
    teams = splitRows[0]
    givenTeamIndex = 1
    for t in teams:
        if t == teamName:
            #teams.remove(t)
            break
        givenTeamIndex += 1

    points = []

    #splitRows[givenTeamIndex].pop(givenTeamIndex)
    splitRows[givenTeamIndex].pop(0)

    for p in splitRows[givenTeamIndex]:
        if p != '':
            points.append(int(p))

    pointsFor = OrderedDict((teams[i], points[i]) for i in range(len(teams) - 1))

    f.close()
    return pointsFor

def getAxis(team):
    t = sortData(team)
    return list(t.keys()),list(t.values())


def numToCoord(n,r,c):
    x = ((n-1) % r) + 1
    y = (n-1)//c + 1

    return x , y


def showLinePlot(teams):
    fig = go.Figure()
    drawBar = len(teams) < 4
    n = 1
    for team in teams:
        t,p = getAxis(team)

        if drawBar:
            sc = go.Bar(x=t, y=p,name = team)
        else:
            sc = go.Scatter(x = t, y = p, name = team)
        n += 1
        fig.add_trace(sc)


    fig.update_layout(title='Teams Points for',
                       xaxis_title='Teams',
                       yaxis_title='Points')


    fig.show()

def main():
    i = 1
    for t in ALLTEAMS:
        print(str(i) + ". " + t)
        i += 1

    print("21. ALL")
    print("22. TOP 6")

    print("Enter the numbers for the teams you would like to include in the plot")
    indexes = input("Input numbers: ").split(",")
    if indexes[0] == "21":
        showLinePlot(ALLTEAMS)
    elif indexes[0] == "22":
        showLinePlot(TOP6)
    else:
        selectedTeams = [ALLTEAMS[int(x) - 1] for x in indexes]
        showLinePlot(selectedTeams)

if __name__ == '__main__':
    main()