myShapeSize = 900
myShapeCount = 23

# move my (0, 0) to the center of the canvas
translate(width()/2, height()/2)
# draw a shape, subtracting half of size from x, y so it draws from center

for myShapeNumber in range(myShapeCount):
    fill(None)
    strokeWidth(5)
    stroke(0)
    rect(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)
    scale(.9)
    rotate(7)
    skew(7)

fontSize(100)
text('hello world', (0, 0))