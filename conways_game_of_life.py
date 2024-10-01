import random, time, copy
width = 60
height = 20

#Create a list of list for the cells:
nextCells = []
for x in range(width):
    column = [] #Create a new column
    for y in range(height):
        if random.randint(0, 1) == 0:
            column.append('#') #Add a living cell
        else:
            column.append(' ') #Add a dead cell
    nextCells.append(column) #nextCells is a list of column lists

while True:
    #Main program loop
    print('\n\n\n\n\n') #Separate each step with newlines
    currentCells = copy.deepcopy(nextCells)
    #Print currenCells on screen:
    for y in range(height):
        for x in range(width):
            print(currentCells[x][y], end='') #Print the # or space
        print() #Print a newline at end of the row

    #Calculate next step's cells based on current step's cells:
    for x in range(width):
        for y in range(height):
            #Get neighboring coordinates:
            #%width  ensures leftCoord is always between 0 and width - 1
            leftCoord = (x - 1) % width
            rightCoord = (x + 1) % width
            aboveCoord = (y - 1) % height
            belowCoord = (y + 1) % height

            #Count number of living neighbors
            numNeighbors = 0
            if currentCells [leftCoord][aboveCoord] == '#':
                numNeighbors += 1 #Top-left neighbor is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors =+ 1
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors =+ 1
            if currentCells[leftCoord][y] == '#':
                numNeighbors =+ 1
            if currentCells[rightCoord][y] == '#':
                numNeighbors =+ 1
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors =+ 1
            if currentCells[x][belowCoord] == '#':
                numNeighbors =+ 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors =+ 1

            #Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                #Living cells with 2 or 3 neighbors stay alive
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                #Dead cells with 3 neighbors become alive
                nextCells [x][y] = '#'
            else:
                #Everything else dies or stays dead
                nextCells[x][y] = ' '
        time.sleep(1) #Add a 1 second pause to reduce flickering