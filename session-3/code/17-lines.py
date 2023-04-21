# stroke settings
stroke(0)
strokeWidth(10)
lineCap('round')

# how many lines to draw
myLineCount = 500

# loop through the number of lines
for myLineNumber in range(myLineCount):
    # determine random coordinates for point 1
    myX1 = randint(0, width())
    myY1 = randint(0, height())
    # determine random coordinates for point 2
    myX2 = randint(0, width())
    myY2 = randint(0, height())
    
    # set the stroke color to random
    stroke(random(), random(), random())
    
    # draw the line
    # including both (x, y) pair as their own tuple
    line((myX1, myY1), (myX2, myY2))