stroke(0)
strokeWidth(20)
lineCap('round')

translate(width()/2, 0)

myBranchHeight = 100
line((0, 0), (0, myBranchHeight))

translate(0, myBranchHeight)

myAngleList = [-30, 30]

for myAngle in myAngleList:
    with savedState():
        rotate(myAngle)
        line((0, 0), (0, myBranchHeight))

