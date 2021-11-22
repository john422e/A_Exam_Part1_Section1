from random import choice, randrange

eventGen = input("BUILD EVENTS? y/n: ")

if eventGen.upper() == 'Y':
    grid = {
        'A': [1, 2, 3, 4, 5, 6],
        'B': [1, 2, 3, 4, 5, 6],
        'C': [1, 2, 3, 4, 5, 6],
        'D': [1, 2, 3, 4, 5, 6],
    }

    while True:
        rows = list(grid.keys())
        row = choice(rows)
        rowList = grid[row].copy()
        if len(rowList) > 1:
            #print("CHOOSING START FROM:", rowList)
            c1 = choice(rowList)
            rowList.remove(c1)
            #print("CHOOSING END FROM:", rowList)
            c2 = choice(rowList)
            if c1 > c2:
                step = -1
            else:
                step = 1

            # now remove everything between selections from master list
            #print("ORIGINAL ROW:", grid[row])
            #print("RANGE:", c1, c2)
            print("ROW:", row)
            for i in range(c1, c2+step, step):
                if i in grid[row]:
                    grid[row].remove(i)
                    print(i)
                else:
                    print("BREAKING AT:", i)
                    break
            #print("UPDATED ROW:", grid[row])
            input()
        else:
            print("row too small")
            input()
        print("CURRENT STATE:")
        for key, val in grid.items():
            print(key, val)

timingGen = input("GET EVENT TIMINGS? y/n ")

if timingGen.upper() == 'Y':
    numEvents = int(input('NUMBER OF EVENTS: '))
    durations = [3+i for i in range(numEvents+4)]

    for event in range(1, numEvents+1):
        print()
        print("EVENT NO.", event)
        duration = choice(durations) # no more than 1/3 of the hour
        durations.remove(duration)
        buffer = 3
        startMax = 60-duration-buffer
        offset1 = randrange(0, 59)
        offset2 = randrange(0, 59)
        startTime = randrange(buffer, startMax)
        endTime = [startTime + duration, offset2] # minutes, seconds
        startTime = [startTime, offset1] # minutes, seconds
        print(startTime, duration, endTime)
