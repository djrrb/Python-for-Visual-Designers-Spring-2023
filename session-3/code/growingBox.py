myFrameCount = 10
myForegroundColor = 0
myBackgroundColor = 1

for mySequenceNumber in range(2):
    # code at this indent will be run once per sequence
    myShapeSize = 100

    for myFrameNumber in range(myFrameCount):
        # code at this indent will be run once per frame per sequence

        newPage()
        # draw background
        fill(myBackgroundColor)
        rect(0, 0, width(), height())
        # move to center of canvas
        translate(width()/2, height()/2)
        
        # draw foreground
        fill(myForegroundColor)
        #rect(-50, -50, 100, 100)

        rect(
            -myShapeSize/2, # x offset
            -myShapeSize/2, # y offset
             myShapeSize, # width
             myShapeSize # height
         )
        
        # draw a red dot in the center
        fill(1, 0, 0)
        oval(-5, -5, 10, 10)
    
        # augment
        myShapeSize += 100 # myShapeSize = myShapeSize + 100
    # swap colors for next phase
    myForegroundColor = 1
    myBackgroundColor = 0

saveImage('growingBox.gif')