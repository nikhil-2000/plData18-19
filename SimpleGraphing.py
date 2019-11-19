from prettytable import PrettyTable
from collections import OrderedDict


ALLTEAMS = ['Arsenal', 'Bournemouth', 'Brighton', 'Burnley', 'Cardiff City', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Huddersfield Town', 'Leicester City', 'Liverpool', 'Man City', 'Man Utd', 'Newcastle United', 'Southampton', 'Spurs', 'Watford', 'West Ham', 'Wolves']

def evalPoints(result):
    h = int(result[1])
    a = int(result[2])
    if h > a:
        return 3,0
    elif h < a:
        return 0,3
    else:
        return 1,1

def cleanDict():
    return OrderedDict((team,0) for team in ALLTEAMS)


def readResults():

    pointsTable = OrderedDict((team,cleanDict()) for team in ALLTEAMS)

    res = open('Results.csv','r',encoding='utf-8-sig')
    splitResults = res.read().split('\n')
    splitResults.pop()
    a=0
    
    for result in splitResults:
        result = result.split(',')
        homePoints,awayPoints = evalPoints(result)
        pointsTable[result[0]][result[3]] += homePoints
        
        pointsTable[result[3]][result[0]] += awayPoints
        if pointsTable['Arsenal']['Arsenal'] > 0:
            print(result)


    return pointsTable

def writeToFile(pointsTable):
    f = open('AllPoints.csv','w')
    f.write("Teams ,")
    for team in ALLTEAMS:
        f.write(team + ",")


    for k in pointsTable:
        f.write('\n')
        f.write(k+',')
        for p in pointsTable[k]:
            f.write(str(pointsTable[k][p])+',')

    f.close()


def sortData(teamName):
    f = open('AllPoints.csv','r')

    tRows = f.read().split('\n')

    splitRows = [r.split(',') for r in tRows]
    splitRows[0].pop(0)
    teams = splitRows[0]
    givenTeamIndex = 1
    for t in teams:
        if t == teamName:
            teams.remove(t)
            break
        givenTeamIndex += 1


    points = []
    
    splitRows[givenTeamIndex].pop(givenTeamIndex)
    splitRows[givenTeamIndex].pop(0)


    for p in splitRows[givenTeamIndex]:
        if p != '':
            points.append(int(p))

    
    pointsFor = OrderedDict((teams[i],points[i]) for i in range(len(teams)-1))
    
    f.close()
    return pointsFor

def teamToTable(teamName):
    teamDict = sortData(teamName)

    t = PrettyTable(['Team', 'Points'])
    t.align['Points'] = "l"
    for k in teamDict:
        t.add_row([k,str(teamDict[k]*'+')])

    print( t)




a = readResults()
writeToFile(a)
#teamToTable('Arsenal')
a = sortData('Liverpool')
