fill(0)
rect(0, 0, width(), height())


stroke(1)
strokeWidth(20)
lineCap('round')

translate(width()/2, 0)

myBranchHeight = 100

def myBranch(level=0):
    print(level)
    # vertical line
    line((0, 0), (0, myBranchHeight))
    # move to top of vertical line
    translate(0, myBranchHeight)

    myAngleList = [-30, 30]
    # if we are within our allowed levels
    # keep drawing other lines at an angle
    if level < 5:
        for myAngle in myAngleList:
            with savedState():
                rotate(myAngle)
                #line((0, 0), (0, myBranchHeight))
                myBranch(level+1)

myBranch()