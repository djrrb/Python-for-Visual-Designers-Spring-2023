myFrameCount = 10 # how many frames
myForegroundColor = 0 # color of the growing shape
myBackgroundColor = 1 # color of the background shape

# loop through the code twice, once for black and once for white
for mySequenceNumber in range(2):
    # code at this indent will be run once per sequence
    # reset the initial shape size to 100, this will grow over time
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
    # dedent, now this code will be run once per sequence
    # swap colors for next phase
    myForegroundColor = 1
    myBackgroundColor = 0

# dedent, this code will be run once
# save the result
saveImage('growingBox.gif')