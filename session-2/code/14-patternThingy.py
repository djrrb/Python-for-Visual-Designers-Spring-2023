# our first shape will be the width of the canvas
myShapeSize = width()
# how many shapes to draw
myShapeCount = 100
# how many frames to draw
myFrameCount = 360//3
myRotationChange = 0
# this code gets run one time
for myFrameNumber in range(myFrameCount):
    # this code gets run myFrameCount times
    # once per frame
    newPage()
    frameDuration(1/12)
    translate(width()/2, height()/2)

    for myShapeNumber in range(myShapeCount):
        # this code gets run myShapeCount*myFrameCount times
        # once per shape per frame
        
        print(myShapeNumber, myShapeNumber // 2, myShapeNumber % 2)
        if myShapeNumber == 8:
            # for shape #8, set the fill to white
            fill(0)
        elif myShapeNumber % 2:
            # otherwise if the shape Number is odd, set to random
            #fill(random(), random(), random(), 1)
            fill(1, 0, 0)
        else:
            # otherwise set to black
            fill(0, 1)
        # draw the shape, centered on (0, 0) (which is in the middle)
        rect(-width()/2, -height()/2, width(), height())
        # for next time, adjust the canvas settings
        # make everything a little smaller
        scale(.95)
        # rotate around (0, 0) by 1 plus myRotationChange
        rotate(1+myRotationChange)
    
    # once per frame, augment our rotation change by a certain number of degrees
    myRotationChange += 90/myFrameCount
        
#save as gif or mp4
saveImage('myPattern.gif')