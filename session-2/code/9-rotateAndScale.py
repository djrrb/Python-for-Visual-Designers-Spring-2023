# perform canvas transfomations
myShapeSize = 700
# move (0, 0) to the center of the canvas
translate(width()/2, height()/2)
# rotate by 45 degrees
rotate(45)
# scale the canvas so all future
# things are stretched horizontally
scale(1, .5)
# draw rectangle in center of canvas
rect(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)

# make a dot in the center of the canvas
fill(1, 0, 0)
oval(-10, -10, 20, 20)

# draw some text
fill(0, 1, 1)
fontSize(100)
text('hello world', (0, 0))