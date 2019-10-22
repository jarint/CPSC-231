# CPSC 231
# Name: Jarin Thundathil
# Tutorial: Shauvik Shadman
# ID: 10149776
# Date: 2019-03-24
# Description: Assignment 1
 
#need to import the turtle interface to begin
import turtle
 
#Defining Constants
WIDTH = 800
HEIGHT = 600
MIDDLEX = WIDTH/2
MIDDLEY = HEIGHT/2
ORIGIN = (WIDTH/2, HEIGHT/2)
 
#Environment setup, as per assignment instructions
pointer = turtle.Turtle()
screen = turtle.getscreen()
screen.setup(WIDTH, HEIGHT, 0, 0)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
pointer.hideturtle()

#Increase turtle speed
turtle.speed("fastest")

#Drawing axes in x and y plane
#Dont want to draw in wrong place so lift the pen
pointer.up()
#Go to X axis start point
pointer.goto(MIDDLEX, MIDDLEY)
#Put pen down
pointer.down()
#begin drawing line in both directions
pointer.goto(800,MIDDLEY)
pointer.up()
pointer.goto(ORIGIN)
pointer.down()
pointer.goto(0,MIDDLEY)
pointer.up()
pointer.goto(ORIGIN)
#Draw vertical axis in same way
pointer.down()
pointer.goto(MIDDLEX, 600)
pointer.up()
pointer.goto(ORIGIN)
pointer.down()
pointer.goto(MIDDLEX, 0)
pointer.up()
pointer.goto(ORIGIN)

#Alert user to program function in preparation for prompts
print("This program takes your input to draw a circle and a line on the screen you see.")
print("Once drawn, the program will tell you if the line intersects with the circle.")
print("If intersects are found, the program will draw small circles at the points of intersection.")
print("The bottom left corner of the screen is (0,0), the axes intersect at (400,300), and the top right corner is (800,600)")

#set up variables such that inputs are integers that are cast to coordinates(except radius, which is a float).
xc = int(input("Enter x of centre of circle: "))
yc = int(input("Enter y of centre of circle: "))
r = float(input("Enter numerical value of circle radius: "))
x1 = int(input("Enter x of line start-point: "))
y1 = int(input("Enter y of line start-point: "))
x2 = int(input("Enter x of line end-point: "))
y2 = int(input("Enter y of line end-point: "))

#Draw the line first. We change colour here so that it is distinguished from the axes.
pointer.color("blue")
pointer.up()
pointer.goto(x1,y1)
pointer.down()
pointer.goto(x2,y2)
pointer.up()

#Draw the circle. Change of color here too.
pointer.color("red")
pointer.goto(xc,(yc-r))
pointer.down()
pointer.circle(r)
pointer.up()

#Input calculations that determine the points of intersection, as per assignment instructions.
a = ((x2-x1)**2) + ((y2-y1)**2)
b = 2*(((x1-xc)*(x2-x1))+((y1-yc)*(y2-y1)))
c = ((x1-xc)**2)+((y1-yc)**2)-(r**2)

#Input quadratic equation to calculate 'alpha'. First, we must calculate the discriminant (portion under the sqrt).
d = (b**2) - (4*a*c)

#Import math functions so you can do sqrt's later.
import math

#write if statements to determine number of intersections and what to output on screen.
if d < 0:
    #print no intersection when d < 0
    print("no intersections")
    pointer.color("green")
    pointer.up()
    pointer.goto(xc,yc)
    #to indicate no intersections are present, write this on the centre of the graphic.
    pointer.write("No Intersection!", move = False, align = "center", font = ("Arial",8,"normal"))
    
#if intersects are present, calculate points of intersection according to assignment instructions, depependent on value of discriminant. 
elif d ==0:
    #calculate 'alpha' for the positive part of the quadratic equation (only one intersection).
    alpha = (-b+math.sqrt(d))/(2*a)
    #calculate x,y coordinates for intersection.
    x = ((1-alpha)*(x1)) + ((alpha)*(x2))
    y = ((1-alpha)*(y1)) + ((alpha)*(y2))
    #set radius of intersect circle to 5.
    ri = 5
    #Draw intersect circle.
    pointer.color("red")
    pointer.goto(x,(y-ri))
    pointer.down()
    pointer.circle(ri)
    pointer.up()
        
#Case where d > 0 
elif d > 0:
    #need to calculate two alphas for positive and negative cases in quadratic formula.
    alpha1 = (-b-math.sqrt(d))/(2*a)
    alpha2 = (-b+math.sqrt(d))/(2*a)
    inter = 0
    #Write if statement to ensure that interseection only drawws if the alpha is between 0 and 1.
    if 0 <= alpha1 <= 1:
        #calculate the first x and y for the first alpha.
        x = ((1-alpha1)*(x1)) + ((alpha1)*(x2))
        y = ((1-alpha1)*(y1)) + ((alpha1)*(y2))
        inter+=1
        #Set radius of intersect circle 1 to 5.
        ri = 5
        #Draw intersect circle.
        pointer.goto(x,(y-ri))
        pointer.down()
        pointer.circle(ri)
        pointer.up()
        
    #Write second if statement to ensure intersects are only drawn if alpha 2 is also between 0 and 1.
    if 0 <= alpha2 <= 1:
        #calculate x and y for alpha 2
        x0 = ((1-alpha2)*(x1)) + ((alpha2)*(x2))
        y0 = ((1-alpha2)*(y1)) + ((alpha2)*(y2))
        inter+=1
        #set intersect circle radius to 5.
        ri = 5
        #Draw intersect circle.
        pointer.goto(x0,(y0-ri))
        pointer.down()
        pointer.circle(ri)
    #print number of intersects.
    print (inter)
        
#end
