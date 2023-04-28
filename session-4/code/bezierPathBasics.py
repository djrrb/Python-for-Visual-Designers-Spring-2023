myPath = BezierPath()

#myPath.rect(0, 0, 100, 100)

#myPath.text('Hello world')

myStripeThickness = 100
myHandleLength = 0
myHandleDiff = 120

myHandle1Diff = randint(-myHandleDiff, myHandleDiff)
myHandle2Diff = randint(-myHandleDiff, myHandleDiff)
print(myHandle1Diff, myHandle2Diff)

myPath.moveTo((0, 0)) # move to lower left
myPath.lineTo((width(), 0)) # draw line across bottom
myPath.lineTo((width(), myStripeThickness))
myPath.curveTo(
    (width(), myStripeThickness+myHandleLength+myHandle1Diff), # handle 1
    (0, myStripeThickness+myHandleLength+myHandle2Diff), # handle 2
    (0, myStripeThickness), # oncurve destination point
    )
myPath.closePath()

stroke(1, 0, 0)
strokeWidth(10)

drawPath(myPath)

fill(0, 1, 0)
stroke(None)
oval(width()-5, myStripeThickness+myHandleLength-5, 10, 10)
oval(-5, myStripeThickness+myHandleLength-5, 10, 10)
#saveImage('textAsPath.pdf')