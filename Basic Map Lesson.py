

## Define a map and let the player move around it
#Define our map: 1 = wall, 0 = path
#0,0 is the top left of the map, therefore...
#moving up decreases the y location and
#moving left decreases the x location and vice versa

Map = [
			[ 1, 1, 1, 1 ],
			[ 1, 0, 1, 1 ],
			[ 1, 0, 1, 1 ],
			[ 1, 0, 0, 1 ],
			[ 1, 0, 1, 1 ],
			[ 1, 1, 1, 1 ]
	]


#Define a function to print our Map and current Player location

def drawMap(currX, currY):
    #print ("map size is : ", len(Map), " rows by ", len(Map[0]), " columns")
    print()
    for y in range (0, len(Map)):
        for x in range (0,len(Map[y])):
            if (currX == x) and (currY == y):   #print * if they are in this square
                print("*  ", end="")
            else:
                print (Map[y][x]," ", end ="")
        print()
    print()
    

#Define our function that will move the player
#The function will first check if the player can move or hits a wall
#If the player can move, then the current location will be updated
#If the player cannot move due to a wall, the location will not be updated
    
def movePlayer(x,y,moveDir):
    #assume invalid move is attempted
    badMove = True

    #Now check if the move is valid - brute force method - better ways exist
    if moveDir == "u":
        if Map[y-1][x] == 0:
            #print ("valid up move")
            return (x, y-1)

    if moveDir == "d":
        if Map[y+1][x] == 0:
            #print ("valid down move")
            return (x, y+1)

    if moveDir == "l":
        if Map[y][x-1] == 0:
            #print ("valid left move")
            return (x-1, y)

    if moveDir == "r":
        if Map[y][x+1] == 0:
            #print ("valid right move")
            return (x+1, y)
        
    #they attempted a bad move
    if badMove:
        print ("**Invalid move** Try again.")
        return (x,y)   #return the same location they are in since no move



#Set our starting location
currX = 1
currY = 4

#draw the map the first time before asking for a move
drawMap(currX, currY)

#Forever just let the player move around the map on the path
while True:
    moveDir = input("Enter direction (u,d,l,r): ")
    currX, currY = movePlayer(currX, currY, moveDir)
    drawMap(currX, currY)
    
