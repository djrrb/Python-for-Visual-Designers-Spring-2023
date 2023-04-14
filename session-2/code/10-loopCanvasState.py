# what is the starting shape size
# this will scale down
myShapeSize = 900
# how many shapes should we draw
myShapeCount = 100

# move my (0, 0) to the center of the canvas
translate(width()/2, height()/2)
# draw a shape, subtracting half of size from x, y so it draws from center

# loop through each shape in our count
for myShapeNumber in range(myShapeCount):
    # set the interior fill to nothing
    fill(None)
    # set a 5pt black stroke
    strokeWidth(5)
    stroke(0)
    # draw the rectangle centered on (0, 0)
    rect(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)
    # for next time, do some canvas transformations
    scale(.9)
    # rotate
    rotate(7)
    #skew(7)