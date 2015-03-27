from graphics import *
import random

# Read in and print out the data in the data file
datafile = open("data.txt",'r')

# Do some simple drawing
window = GraphWin("Visualisation", 500, 500)

count = 1
for line in datafile:
    
    print(line)
    circleSize = float(line)
    
    ball = Circle(Point(500-count, 500-count), circleSize)
    ball2 = Circle(Point(0+count, 0+count), circleSize)
    ball3 = Circle(Point(500-count, 0+count), circleSize)
    ball4 = Circle(Point(0+count, 500-count), circleSize)

    #ball.setFill(color_rgb(0,0,0))
    
    count += 10
    ball.draw(window)
    ball2.draw(window)
    ball3.draw(window)
    ball4.draw(window)
  
# Waits until the mouse is clicked before closing the window
window.getMouse()
    
