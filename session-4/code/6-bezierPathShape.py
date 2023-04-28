# set some variables
myStripeThickness = 100
myHandleLength = 0
myHandleDiff = 120

# make an empty path
myPath = BezierPath()

# calculate two random numbers to vary the handle length
myHandle1Diff = randint(-myHandleDiff, myHandleDiff)
myHandle2Diff = randint(-myHandleDiff, myHandleDiff)
print(myHandle1Diff, myHandle2Diff)

# start drawing the bezier path
myPath.moveTo((0, 0)) # move to lower left
myPath.lineTo((width(), 0)) # draw line across bottom
myPath.lineTo((width(), myStripeThickness)) # draw a line up the right side

myPath.curveTo(
    (width(), myStripeThickness+myHandleLength+myHandle1Diff), # handle 1
    (0, myStripeThickness+myHandleLength+myHandle2Diff), # handle 2
    (0, myStripeThickness), # oncurve destination point
    ) # draw the curve
myPath.closePath()  # connect this point to the starting point

# set some canvas formatting
stroke(1, 0, 0)
strokeWidth(10)

# draw the shape
drawPath(myPath)

# draw the dots
fill(1, 0, .5)
stroke(None)
oval(width()-10, myStripeThickness+myHandleLength+myHandle1Diff-10, 20, 20)
oval(-10, myStripeThickness+myHandleLength+myHandle2Diff-10, 20, 20)
#saveImage('textAsPath.pdf')