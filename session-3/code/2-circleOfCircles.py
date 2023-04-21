myShapeSize = 180 # size of each shape
myShapeCount = 20 # how many shapes
myShapeOffset = 180 # how far the shapes are from center

# move (0, 0) to center of canvas
translate(width()/2, height()/2)

# set the blend mode to overlay
# so that we can see the overlap of the shapes
blendMode('overlay')

# loop through the number of shapes
for myShapeNumber in range(myShapeCount):
    # set the fill to random
    fill(random(), random(), random())
    
    # draw the oval
    # subtracting half the size (myShapeSize/2)
    # means we are drawing from the center of the circle
    # adding myShapeOffset to Y moves the whole thing 
    # up and away from the center of the canvas
    
    oval(
        -myShapeSize/2, # x 
        -myShapeSize/2+myShapeOffset, # y
        myShapeSize, # width
        myShapeSize # height
    )
    # now rotate the canvas
    # if we divide 360 by my shape count
    # we will get the number of degrees necessary
    # to have our shapeCount complete a full circle
    rotate(360/myShapeCount)
    

# my guide dot
fill(1, 0, 0)
oval(-5, -5, 10, 10)

# save result
saveImage('circleOfCircles.pdf')