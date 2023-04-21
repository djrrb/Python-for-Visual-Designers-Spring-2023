myShapeSize = 180
myShapeCount = 20
myShapeOffset = 180

# move to center
translate(width()/2, height()/2)

blendMode('overlay')

for myShapeNumber in range(myShapeCount):
    fill(random(), random(), random())
    oval(
        -myShapeSize/2, 
        -myShapeSize/2+myShapeOffset, 
        myShapeSize, 
        myShapeSize
    )
    rotate(360/myShapeCount)
    
    
# my guide dot
fill(1, 0, 0)
oval(-5, -5, 10, 10)

saveImage('circleOfCircles.pdf')