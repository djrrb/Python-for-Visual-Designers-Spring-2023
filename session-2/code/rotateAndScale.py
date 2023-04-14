myShapeSize = 700
translate(width()/2, height()/2)
rotate(45)
scale(1, .5)
#rect(-450, -450, 900, 900)
rect(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)

fill(1, 0, 0)
oval(-10, -10, 20, 20)

fill(0, 1, 1)
fontSize(100)
text('hello world', (0, 0))