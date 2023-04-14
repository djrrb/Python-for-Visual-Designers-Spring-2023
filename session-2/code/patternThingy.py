myShapeSize = width()
myShapeCount = 100
myFrameCount = 10
myRotationChange = 0
# this code gets run one time
for myFrameNumber in range(myFrameCount):
    # this code gets run 10 times
    # once per frame
    newPage()
    frameDuration(1/12)
    translate(width()/2, height()/2)

    for myShapeNumber in range(myShapeCount):
        # this code gets run 1000 times
        # once per shape per frame
        
        print(myShapeNumber, myShapeNumber // 2, myShapeNumber % 2)
        if myShapeNumber == 8:
            fill(1, 1)
        elif myShapeNumber % 2:
            fill(random(), random(), random(), 1)
        else:
            fill(0, 1)
        rect(-width()/2, -height()/2, width(), height())
        #oval(50, 350, 1000, 1000)
        # polygon(
        #     (0, 0),
        #     (500, 0),
        #     (450, 300),
        #     (0, 380)
        #     )

        scale(.95)
        rotate(1+myRotationChange)
    
    myRotationChange += 90/myFrameCount
        
saveImage('myPattern.gif')