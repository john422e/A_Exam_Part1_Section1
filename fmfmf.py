from datetime import time, timedelta
import os
import matplotlib.pyplot as plt
import numpy as np

def makeDelta(t1, t2):
    # t2 is the most recent time
    d1 = timedelta(hours=t1[0], minutes=t1[1], seconds=t1[2])
    d2 = timedelta(hours=t2[0], minutes=t2[1], seconds=t2[2])
    dur = d2-d1
    return dur


# event = [ t1, t2, duration, material, location, hand ]
H = 'wood'
P = 'paper'
L = 'left'
R = 'right'
A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'

# 30 events
score = [
    [   [0,20,51], [0,21,25], [ 0,34], H, [C, 5, 2], L ], #1
    [   [0,42,45], [0,44,14], [ 1,29], H, [D, 5, 4], L ], #2
    [   [0,53, 6], [1, 3,16], [10,10], H, [C, 3, 1], L ], #3
    [   [1,20,50], [1,21, 3], [ 0,13], P, [E, 1, 5], R ], #4
    [   [1,40,14], [1,40,17], [ 0, 3], H, [B, 3, 5], R ], #5
    [   [1,48,19], [1,48,24], [ 0, 5], H, [C, 1, 4], R ], #6
    [   [2, 8, 0], [2, 8, 2], [ 0, 2], H, [D, 2, 1], L ], #7
    [   [2,31,16], [2,32,11], [ 0,55], P, [D, 5, 1], L ], #8
    [   [2,51,17], [2,52,12], [ 0,55], H, [B, 1, 5], R ], #9
    [   [3,16,14], [3,16,16], [ 0, 2], P, [B, 5, 1], L ], #10
    [   [3,27, 6], [3,28, 1], [ 0,55], H, [C, 1, 5], R ], #11
    [   [3,38, 7], [3,40,31], [ 2,24], H, [B, 2, 1], L ], #12
    [   [3,51,53], [3,52,27], [ 0,34], H, [C, 5, 4], L ], #13
    [   [4, 2,35], [4, 3, 9], [ 0,34], P, [A, 5, 1], L ], #14
    [   [4,16,10], [4,16,11], [ 0, 1], H, [A, 4, 5], R ], #15
    [   [4,27, 1], [4,27,35], [ 0,34], H, [D, 5, 1], L ], #16
    [   [4,52,30], [4,58,47], [ 6,17], P, [B, 4, 2], L ], #17
    [   [5, 9,14], [5,11,38], [ 2,24], P, [B, 1, 5], R ], #18
    [   [5,26,30], [5,26,51], [ 0,21], P, [A, 1, 3], R ], #19
    [   [5,40,31], [5,42, 0], [ 1,29], P, [A, 5, 1], L ], #20
    [   [5,55, 8], [6, 5,18], [10,10], P, [E, 3, 5], R ], #21
    [   [6, 3,50], [6, 4,45], [ 0,55], H, [D, 5, 1], L ], #22
    [   [6,24,32], [6,24,35], [ 0, 3], H, [A, 1, 2], R ], #23
    [   [6,41,50], [6,44,14], [ 2,24], P, [E, 1, 2], R ], #24
    [   [7, 7,12], [7,13,29], [ 6,17], H, [E, 5, 4], L ], #25
    [   [7,33,31], [7,35, 0], [ 1,29], H, [D, 3, 4], R ], #26
    [   [7,41,47], [7,41,50], [ 0, 3], H, [E, 5, 2], L ], #27
    [   [8, 1,16], [8, 1,17], [ 0, 1], H, [A, 4, 3], L ], #28
    [   [8,28,16], [8,28,19], [ 0, 3], H, [C, 1, 4], R ], #29
    [   [8,43, 2], [8,44,31], [ 1,29], P, [C, 2, 5], R ] #30
]

pieceLength = timedelta(hours=9)
totalPlaying = timedelta()
totalWood = 0
totalPaper = 0
totalLeft = 0
totalRight = 0
totalRows = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0
}
totalDistance = 0
#rows = ['', 'A', 'B', 'C', 'D', 'E', '']
rows = ['', 'E', 'D', 'C', 'B', 'A', '']
rowCounts = [0 for i in range(5)]
rowColors = [0.8 for i in range(5)]
plots = [ [] for i in range(30) ]


rates = []
totalRate = 0

for i, event in enumerate(score):
    dur = makeDelta(event[0], event[1])
    event[2] = dur
    durSeconds = int(dur.seconds)
    totalPlaying += dur
    # tally wood/paper
    if event[3] == H:
        totalWood += 1
    else:
        totalPaper += 1
    # tally L/R
    if event[5] == L:
        totalLeft += 1
    else:
        totalRight += 1
    # tally row
    row = event[4][0]
    totalRows[row] += 1
    # get distance travelled
    line = (event[4][1], event[4][2])
    lineMax = max(line)
    lineMin = min(line)
    distance = lineMax - lineMin
    totalDistance += distance
    # CALCULATE A VALUE RELATING DISTANCE TO DURATION (rate)
    rate = distance / durSeconds
    totalRate += rate
    print("RATE (squares/second): ", rate, distance, durSeconds, "material: ", event[3])
    rates.append(rate)
    # plot line
    y = rows.index(row)
    if(event[3]) == H:
        lstyle = 'solid'
        lwidth = 10
        color = 1 - (rate * 0.4) - 0.1
    else:
        lstyle = (0, (0.3, 0.05))
        lwidth = 15
        color = 1 - (rate * 0.4) - 0.1

    #print("COLOR:", color)

    #lineInfo = [[lineMin, lineMax], [y+rowCounts[y], y+rowCounts[y]], lstyle, lwidth, 'gray']
    lineInfo = [[lineMin, lineMax], [y, y], lstyle, lwidth, str(color)]
    if i == 0:
        plots[i].append(lineInfo)
    else:
        plots[i] = plots[i-1].copy()
        plots[i].append(lineInfo)

    #rowCounts[y-1] += 1#0.15
    #rowColors[y-1] -= 0.1
    #print(dur, totalPlaying)
    #input()

eventPlots = input('TOTAL EVENT ANALYSIS: make plots? y/n: ')
if eventPlots.upper() == 'Y':
    path = 'analysis'
    if not os.path.exists(path):
        os.makedirs(path)
    path += '/visuals'
    if not os.path.exists(path):
        os.makedirs(path)
    path += '/eventPlots'
    if not os.path.exists(path):
        os.makedirs(path)

    for i, plot in enumerate(plots):
        plt.rcParams['figure.figsize'] = [2.2, 1.7]
        for line in plot:
            plt.plot(line[0], line[1], linestyle=line[2], linewidth=line[3], color=line[4])
        plt.yticks([0, 1, 2, 3, 4, 5, 6], rows)
        plt.xticks([1, 2, 3, 4, 5], ['1' ,'2', '3', '4', '5'])
        #plt.title('After event ' + str(i+1))
        plt.title(str(score[i][2].seconds) + " sec, " + str(score[i][3]) + ", " + str(score[i][4][0]) + " " + str(score[i][4][1]) + "-" + str(score[i][4][2]))
        plt.savefig(path + '/event' + str(i+1) + '.png', bbox_inches='tight')

totalSilence = pieceLength - totalPlaying
print("LENTHS:", pieceLength, totalPlaying, totalSilence, "AVG:", totalPlaying/30)
print("WOOD:", totalWood, "PAPER:", totalPaper)
print("LEFT:", totalLeft, "RIGHT:", totalRight)
for row, total in totalRows.items():
    print(row, total)
print("AVERAGE DISTANCE:", totalDistance/30)
print("minRate: ", min(rates), "max: ", max(rates), "avg: ", totalRate/30)


# --------------------------------------------------
# do everything again but this time account for time and fade out color over time


pieceLength = timedelta(hours=9)
totalPlaying = timedelta()
totalWood = 0
totalPaper = 0
totalLeft = 0
totalRight = 0
totalRows = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0
}
totalDistance = 0
plots = [ [] for i in range(30) ]



for i, event in enumerate(score):
    dur = makeDelta(event[0], event[1])
    event[2] = dur
    durSeconds = int(dur.seconds)
    totalPlaying += dur
    # tally wood/paper
    if event[3] == H:
        totalWood += 1
    else:
        totalPaper += 1
    # tally L/R
    if event[5] == L:
        totalLeft += 1
    else:
        totalRight += 1
    # tally row
    row = event[4][0]
    totalRows[row] += 1
    # get distance travelled
    line = (event[4][1], event[4][2])
    lineMax = max(line)
    lineMin = min(line)
    distance = lineMax - lineMin
    totalDistance += distance
    # CALCULATE A VALUE RELATING DISTANCE TO DURATION (rate)
    rate = distance / durSeconds
    print("RATE:", rate, distance, durSeconds)
    # plot line
    y = rows.index(row)
    if(event[3]) == H:
        lstyle = 'solid'
        lwidth = 10
        color = 1 - (rate * 0.4) - 0.1
    else:
        lstyle = (0, (0.3, 0.05))
        lwidth = 15
        color = 1 - (rate * 0.4) - 0.1

    #print("COLOR:", color)

    #lineInfo = [[lineMin, lineMax], [y+rowCounts[y], y+rowCounts[y]], lstyle, lwidth, 'gray']
    lineInfo = [[lineMin, lineMax], [y, y], lstyle, lwidth, str(color)]
    if i == 0:
        plots[i].append(lineInfo)
    else:
        plots[i] = plots[i-1].copy()
        plots[i].append(lineInfo)

    #rowCounts[y-1] += 1#0.15
    #rowColors[y-1] -= 0.1
    #print(dur, totalPlaying)
    #input()

eventPlots = input('TIME EVENT ANALYSIS: make plots? y/n: ')
if eventPlots.upper() == 'Y':
    path = 'analysis'
    if not os.path.exists(path):
        os.makedirs(path)
    path += '/visuals'
    if not os.path.exists(path):
        os.makedirs(path)
    path += '/timedEventPlots'
    if not os.path.exists(path):
        os.makedirs(path)

    for i, plot in enumerate(plots):
        # 0 - 29
        plt.rcParams['figure.figsize'] = [2.2, 1.7]

        currentTime = score[i][0] # beginning of newest event
        #currentTime = timedelta(hours=currentTime[0], minutes=currentTime[1], seconds=currentTime[2])

        for j, line in enumerate(plot):
            # get color
            color = float(line[4])
            diffTime = 0 # preset
            if i > 0:
                if i != j:
                    # calculate color fade here
                    oldTime = score[j][1] # when event ended
                    #oldTime = timedelta(hours=oldTime[0], minutes=oldTime[1], seconds=oldTime[2])
                    diffTime = int(makeDelta(oldTime, currentTime).seconds)
                    if (i==21 and j==20): # exception for this 1 time where there is overlap
                        diffTime = int(makeDelta(currentTime, oldTime).seconds)
                    #print(i, j)
                    #print(currentTime, oldTime)
                    #print("TIME SINCE LAST EVENT ENDED:", diffTime)
                    if diffTime > 600:
                        color = 1 # anything more than 10 minutes ago becomes white
                        #oldColor = color
                    else:
                        oldColor = color
                        whiteRemainder = 1 - color
                        # the more this remainder is shrunk, the less fade there is
                        # so we want bigger values for smaller time diffs (0-1)
                        whiteRemainder *= ( 1 / (600 - diffTime) )
                        color += whiteRemainder
                    #print("COLOR:", color, oldColor)
                    #input()

            plt.plot(line[0], line[1], linestyle=line[2], linewidth=line[3], color=str(color))
        plt.yticks([0, 1, 2, 3, 4, 5, 6], rows)
        plt.xticks([1, 2, 3, 4, 5], ['1' ,'2', '3', '4', '5'])
        #plt.title('After event ' + str(i+1))
        eventTime = score[i][0]
        minutes = eventTime[1]
        seconds = eventTime[2]
        if minutes < 10:
            minutes = "0" + str(minutes)
        else:
            minutes = str(minutes)
        if seconds < 10:
            seconds = "0" + str(seconds)
        else:
            seconds = str(seconds)
        displayTime = str(eventTime[0]) + ":" + minutes + ":" + str(seconds)
        plt.title(displayTime + ", " + str(score[i][3]) + ", " + str(score[i][4][0]) + " " + str(score[i][4][1]) + "-" + str(score[i][4][2]))
        plt.savefig(path + '/event' + str(i+1) + '.png', bbox_inches='tight')

totalSilence = pieceLength - totalPlaying
print("LENTHS:", pieceLength, totalPlaying, totalSilence, "AVG:", totalPlaying/30)
print("WOOD:", totalWood, "PAPER:", totalPaper)
print("LEFT:", totalLeft, "RIGHT:", totalRight)
for row, total in totalRows.items():
    print(row, total)
print("AVERAGE DISTANCE:", totalDistance/30)
