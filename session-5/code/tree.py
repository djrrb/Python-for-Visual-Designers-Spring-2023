# set the stroke settings
stroke(0) # stroke color (0=black)
strokeWidth(20) # stroke thickness
lineCap('round') # line cap

# move to horizontal center
translate(width()/2, 0)

# draw a vertical line to represent a branch
myBranchHeight = 100
line((0, 0), (0, myBranchHeight))

# move (0, 0) to the top of the branch
translate(0, myBranchHeight)

# determine which angles to draw at
myAngleList = [-30, 30]

# loop through angles
for myAngle in myAngleList:
    # save state so further rotation is localized
    with savedState():
        # rotate by the amount
        rotate(myAngle)
        # draw another “vertical” line
        # this one will be at an angle 
        line((0, 0), (0, myBranchHeight))

