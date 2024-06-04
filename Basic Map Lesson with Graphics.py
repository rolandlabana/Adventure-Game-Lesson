
import turtle
from turtle import *

sq = Turtle()
sideLength = 50
mapOffset = 400
VISDIST = 2

#Set our starting location
currX = 2
currY = 8


## Define a map and let the player move around it
#Define our map: 1 = wall, 0 = path
#0,0 is the top left of the map, therefore...
#moving up decreases the y location and
#moving left decreases the x location and vice versa

##Map = [
##			[ 1, 1, 1, 1 ],
##			[ 1, 0, 1, 1 ],
##			[ 1, 0, 1, 1 ],
##			[ 1, 0, 0, 1 ],
##			[ 1, 0, 1, 1 ],
##			[ 1, 1, 1, 1 ]
##	]



Map = [
                        [ 1,1, 1, 1, 1, 1, 1,1,1,1,1,1,1,1,1 ,1],
                        [ 1,1, 1, 1, 1, 1, 1,1,1,1,1,1,1,1 ,1,1],
                        [ 1,1, 1, 1, 1, 1, 1,1,1,1,1,1,0,0,1,1 ],
                        [ 1,1, 1, 1, 1, 1, 1,1,0,1,1,1,0,0,1,1 ],
                        [ 1,1, 1, 1, 1, 0, 0,0,0,1,1,1,0 ,0,1,1] ,
                        [ 1,1, 1, 1, 1, 0, 0,0,0,1,1,1,0,1,1,1 ],
                        [ 1,1, 1, 1, 1, 0, 0,0,0,1,1,1,0,1,1,1 ],
			[ 1,1, 1, 1, 1, 1, 1,1,0,1,1,1,0,1,1,1 ],
			[ 1,1, 0, 0, 0, 0, 0,0,0,0,0,0,0,1,1,1 ],
			[ 1,1, 0, 1, 1 ,1, 1,1,1,1,1,1,1,1,1,1],
			[ 1,1, 0, 0, 1,1,  1,1,1,1,1,1,1,1,1,1],
			[ 1,1, 0, 1, 1 ,1],
			[ 1,1, 1, 1, 1 ,1],
                         [1,1, 1,  1, 1, 1]
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

def drawSquare(sideLength):
      
    # start the filling color 
    sq.begin_fill() 
    sq.pendown()
    sq.setheading(0)
    sq.forward(sideLength)
    sq.right(90)
    sq.forward(sideLength)
    sq.right(90)
    sq.forward(sideLength)
    sq.right(90)
    sq.forward(sideLength)
    # ending the filling of the color 
    sq.end_fill()
    return

def drawGraphicsMap(currX, currY):
    for row in range (0, len (Map)):
        for col in range (0, len (Map[row])):
            sq.penup()
            sq.setx(col*sideLength-mapOffset)
            sq.sety(row*-sideLength+mapOffset)
            if (currX == col) and (currY == row): #player spot
                sq.fillcolor("blue")
            elif Map[row][col]==1:
                sq.fillcolor("brown")
            elif Map[row][col]==0:
                sq.fillcolor("yellow")

            #only draw the part of the map visible (todo: also draw visited squares)
            distX = abs(currX - col)
            distY = abs(currY - row)
            #check if within the visible distance
            if (distX <= VISDIST) and (distY <= VISDIST):
                #print(distX, distY)
                #now check if only one is within visible distance
                if ((distX >= VISDIST) and (distY >= VISDIST)):
                    pass   #don't draw
                else:
                    #print("Curr loc: ",currY, currX, end=", ")
                    #don't see through a wall
                    #print("row/col: ", row, col)
                    if (row==0 or col==0): continue
                    if ((distX > 1) and (Map[row][col-1]==1))or ((distY > 1) and (Map[row-1][col]==1)) or ((distX > 1) and (Map[row][col]==1))or ((distY > 1) and (Map[row+1][col]==1)):
                         pass   #print("Don't draw: ", row, col, " : ", Map[row][col-1], Map[row][col], Map[row][col+1]) #don't look past the wall
                    else:
                        #print("Draw: ", row, col)
                        drawSquare(sideLength)

            #sq.penup()
            #sq.setx(col*sideLength+(sideLength/2))
            #sq.sety((row*-sideLength)-(sideLength/2))
            #sq.write("H", move=False)
            #sq.pendown()
            
    screen.update()
    return

    
    

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



screen = turtle.Screen()
screen.title("My window")
screen.bgcolor("white")
screen.tracer(0)

#draw the map the first time before asking for a move
#drawMap(currX, currY)
drawGraphicsMap(currX, currY)
screen.update()
 
#Forever just let the player move around the map on the path
while True:
    moveDir = input("Enter direction (u,d,l,r): ")
    currX, currY = movePlayer(currX, currY, moveDir)
    #drawMap(currX, currY)
    drawGraphicsMap(currX, currY)
   
   
    
