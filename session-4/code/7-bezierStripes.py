myHandleLength = 0 # the basic length of each handle
myHandleDiff = 120 # the random length of each handle
myStripeCount = 12 # the number of stripes to draw

# how tall the stripe should be
# start at the full canvas height, plus some
myStripeThickness = height()+myHandleDiff

# loop through number of stripes
for myStripe in range(myStripeCount):
    # define a new path
    myPath = BezierPath()
    # get two random values to add to handle length
    myHandle1Diff = randint(-myHandleDiff, myHandleDiff)
    myHandle2Diff = randint(-myHandleDiff, myHandleDiff)

    myPath.moveTo((0, 0)) # move to lower left
    myPath.lineTo((width(), 0)) # draw line across bottom
    myPath.lineTo((width(), myStripeThickness)) # draw line up right side
    myPath.curveTo(
        (width(), myStripeThickness+myHandleLength+myHandle1Diff), # handle 1
        (0, myStripeThickness+myHandleLength+myHandle2Diff), # handle 2
        (0, myStripeThickness), # oncurve destination point
        ) # draw curve across top
    myPath.closePath() # connect left top and left bottom sides to close the path

    # set the blend mode
    blendMode('overlay')
    # give us a color
    fill(random(), random(), random(), 1)
    # draw the path
    drawPath(myPath)
    # make the stripe a little shorter each time
    # so that the short ones draw in front of the long ones
    myStripeThickness -= 100

# save image
saveImage('stripes.pdf')