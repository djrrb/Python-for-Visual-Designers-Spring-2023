



myHandleLength = 0
myHandleDiff = 120
myStripeCount = 12
myStripeThickness = height()+myHandleDiff

for myStripe in range(myStripeCount):
    
    myPath = BezierPath()
    myHandle1Diff = randint(-myHandleDiff, myHandleDiff)
    myHandle2Diff = randint(-myHandleDiff, myHandleDiff)
    #print(myHandle1Diff, myHandle2Diff)
    print(myStripeThickness)

    myPath.moveTo((0, 0)) # move to lower left
    myPath.lineTo((width(), 0)) # draw line across bottom
    myPath.lineTo((width(), myStripeThickness))
    myPath.curveTo(
        (width(), myStripeThickness+myHandleLength+myHandle1Diff), # handle 1
        (0, myStripeThickness+myHandleLength+myHandle2Diff), # handle 2
        (0, myStripeThickness), # oncurve destination point
        )
    myPath.closePath()

    blendMode('overlay')
    fill(random(), random(), random(), .5)
    #stroke(0)
    drawPath(myPath)
    
    myStripeThickness -= 100
    
saveImage('stripes.pdf')