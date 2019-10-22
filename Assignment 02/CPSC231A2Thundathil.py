#Name: Jarin Thundathil
#UCID: 10149776
#Course: CPSC231
#Tutorial: 05
#TA: Shauvik Shadman
#Assignment: 02

#Import math function set
from math import *
import turtle

# CONSTANTS
WIDTH = 800
HEIGHT = 600
AXISCOLOR = "black"
TICKLENGTH = 3 #constant defines pixel length of axes tick marks

#Returns the screen (pixel based) coordinates of some (x, y) graph location base on configuration
#Parameters:
#xo, yo : the pixel location of the origin of the  graph
#ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#x, y: the graph location to change into a screen (pixel-based) location
#Usage -> screenCoor(xo, yo, ratio, 1, 0)
#Returns: (screenX, screenY) which is the graph location (x,y) as a pixel location in the window

def screenCoor(xo, yo, ratio, x, y):
    screenX = (xo + ratio * x) #sets screenX variable 
    screenY = (yo + ratio * y) #sets screenY variable
    return ((screenX), (screenY)) #returns screenX and screenY as pixel coordinates

##Returns a string of the colour to use for the current expression being drawn
##This colour is chosen based on which how many expression have previously been drawn
##The counter starts at 0, the first or 0th expression, should be red, the second green, the third blue
##then loops back to red, then green, then blue, again
##Usage -> getColor(counter)
##Parameters:
##counter: an integer where the value is a count (starting at 0) of the expressions drawn
##Returns: 0 -> "red", 1 -> "green", 2 -> "blue", 3 -> "red", 4 -> "green", etc.

def getColor(counter):

    #if statement for when remainder is 0, i.e. first in 1-3 count
    if counter % 3 == 0:
        return "red" #sets colour red
    
    #elif statement for remainder = 1
    elif counter % 3 == 1:
        return "green" #sets colour green

    #elif statement for remainder = 2
    elif counter % 3 == 2:
        return "blue" #sets colour blue

##Draw in the window an xaxis label (text) for a point at (screenX, screenY)
##the actual drawing points will be offset from this location as necessary
##Ex. for (x,y) = (1,0) or x-axis tick/label spot 1, draw a tick mark and the label 1
##Usage -> drawXAxisLabelTick(pointer, 1, 0, "1")
##Parameters:
##pointer: the turtle drawing object
##screenX, screenY): the pixel screen location to drawn the label and tick mark for
##text: the text of the label to draw
##Returns: Nothing
    
def drawXAxisLabelTick(pointer, screenX, screenY, text):
    pointer.goto(screenX, screenY+TICKLENGTH) #draws ticklength on positive y axis across x
    pointer.write(text, False, align = "center") #writes label
    pointer.goto(screenX, screenY - TICKLENGTH) #draws ticklength on negative y axis across x
    pointer.goto(screenX, screenY) #bring pointer back to center

##Draw in the window an yaxis label (text) for a point at (screenX, screenY)
##the actual drawing points will be offset from this location as necessary
##Ex. for (x,y) = (0,1) or y-axis tick/label spot 1, draw a tick mark and the label 1
##Usage -> drawXAxisLabelTick(pointer, 0, 1, "1")
##Parameters:
##pointer: the turtle drawing object
##screenX, screenY): the pixel screen location to drawn the label and tick mark for
##text: the text of the label to draw
##Returns: Nothing

def drawYAxisLabelTick(pointer, screenX, screenY, text):
    pointer.goto(screenX+TICKLENGTH, screenY) #draws ticklength on positive x axis across y
    pointer.write(text, False, align= "center") #writes label
    pointer.goto(screenX-TICKLENGTH, screenY) #draws ticklength on negative x axis across y
    pointer.goto(screenX, screenY) #bring pointer back to center

##Draw in the window an xaxis (secondary function is to return the minimum and maximum graph locations drawn at)
##Usage -> drawXAxis(pointer, xo, yo, ratio)
##Parameters:
##pointer: the turtle drawing object
##xo, yo : the pixel location of the origin of the  graph
##ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
##Returns: (xmin, ymin) where xmin is minimum x location drawn at and xmax is maximum x location drawn at

def drawXAxis(pointer, xo, yo, ratio):
    xmin = xo #set xmin @ origin
    xmax = xo #set xmax @ origin

    #set up pointer
    pointer.up()
    pointer.goto(xo,yo)
    pointer.down()

    counterx1 = 1 #sets counter for positive x axis labels at +1
    #right side of x axis
    while (xmax <= WIDTH):
        xmax = xmax + ratio #sets xmax as xmax+ratio
        pointer.goto(xmax,yo)   #draws axis
        drawXAxisLabelTick(pointer,xmax,yo,str(counterx1))  #draw axis ticks
        counterx1 = counterx1+1 #sets counter x one point higher per iteration

    xmax = counterx1 # set xmax as counterx1 for usage in Draw(expr)
    #set up pointer
    pointer.up()
    pointer.goto(xo,yo)
    pointer.down()  

    counterx2 = -1 #sets counter for negative x axis labels at -1
    #Left side of x axis
    while xmin >= 0:
         xmin = xmin - ratio #sets xmin as xmin-ratio
         pointer.goto(xmin,yo) #draws axis 
         drawXAxisLabelTick(pointer,xmin,yo,str(counterx2)) #draws axis ticks
         counterx2 = counterx2-1 #sets counterx2 to one lower each iteration

    xmin = counterx2 #sets xmin as counterx2 for usage in Draw(expr)

    return xmin, xmax #returns xmin and xmax

##Draw in the window an yaxis 
##Usage -> drawYAxis(pointer, xo, yo, ratio)
##Parameters:
##pointer: the turtle drawing object
##xo, yo : the pixel location of the origin of the  graph
##ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
##Returns: Nothing

def drawYAxis(pointer, xo, yo, ratio):
    ymin = yo
    ymax = yo
    #set up pointer
    pointer.up()
    pointer.goto(xo,yo)
    pointer.down()

    countery1 = 1 #sets label counter to 1 for positive y axis
    #top side of y axis
    while (ymax <= HEIGHT):
        ymax = ymax + ratio
        pointer.goto(xo,ymax)   #draws line
        drawYAxisLabelTick(pointer,xo,ymax,str(countery1))  #draws ticks with earlier function
        countery1 = countery1+1 #adds one to the label counter
        
    #reset pointer
    pointer.up()
    pointer.goto(xo,yo)
    pointer.down()

    countery2 = -1 #sets label counter to -1 for negative y axis
    #bottom side of y axis
    while ymin >= 0:
         ymin = ymin - ratio
         pointer.goto(xo,ymin)  #draws line
         drawYAxisLabelTick(pointer,xo,ymin,str(countery2)) #draws ticks
         countery2 = countery2-1 #adds one to label counter

##Draw in the window the given expression (expr) between [xmin, xmax] graph locations
##Usage -> drawExpr(pointer, xo, yo, ratio, xmin, xmax, expr)
##Parameters:
##pointer: the turtle drawing object
##xo, yo : the pixel location of the origin of the  graph
##ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
##expr: the expression to draw (assumed to be valid)
##xmin, ymin : the range for which to draw the expression [xmin, xmax]
##Returns: Nothing
         
def drawExpr(pointer, xo, yo, ratio, xmin, xmax, expr):
    #Draw expression
    x = xmin 
    DELTA = 0.1 #smooths curve so values calculated at 10 points between tick marks

    #set up pointer
    pointer.up()
    pointer.goto(xo,yo)
    print(xmin) #prints lower bound for x
    print(xmax) #prints upper bound for x

    #opens while loop for when x is between map edges.
    while (x >= xmin and x<= xmax):

            y = eval(expr) #evaluates based on expression from user
            print("When x is", x, "the value of the expresion is", y)
            screenX, screenY = screenCoor(xo, yo, ratio, x ,y)  #uses earlier function to convert x and y to screen coordinates
            pointer.goto(screenX,screenY)   #draw function
            pointer.down()
            x+=0.1  #adds 0.1 to x for each loop iteration

##Setup of turtle screen before we draw
##DO NOT CHANGE THIS FUNCTION
##Returns: Nothing

def setup():
    pointer = turtle.Turtle()
    screen = turtle.getscreen()
    screen.setup(WIDTH, HEIGHT, 0, 0)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer.hideturtle()
    screen.delay(delay=0)
    return pointer

##Main function that attempts to graph a number of expressions entered by the user
##The user is also able to designate the origin of the chart to be drawn, as well as the ratio of pixels to steps (shared by both x and y axes)
##The window size is always 800 width by 600 height in pixels
##DO NOT CHANGE THIS FUNCTION
##Returns: Nothing

def main():
    #Setup window
    pointer = setup()

    #Get input from user
    xo, yo = eval(input("Enter pixel coordinates of origin: "))
    ratio = int(input("Enter ratio of pixels per step: "))

    #Set color and draw axes (store discovered visible xmin/xmax to use in drawing expressions)
    pointer.color(AXISCOLOR)
    xmin, xmax = drawXAxis(pointer, xo, yo, ratio)
    drawYAxis(pointer, xo, yo, ratio)

    #Loop and draw experssions until empty string "" is entered, change expression colour based on how many expressions have been drawn
    expr = input("Enter an arithmetic expression: ")
    counter = 0
    while expr != "":
        pointer.color(getColor(counter))
        drawExpr(pointer, xo, yo, ratio, xmin, xmax, expr)
        expr = input("Enter an arithmetic expression: ")
        counter += 1
 
#Run the program
main()
