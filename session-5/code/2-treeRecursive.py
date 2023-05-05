# black background
fill(0)
rect(0, 0, width(), height())

# set the stroke settings
stroke(1) # stroke color (0=black)
strokeWidth(20) # stroke thickness
lineCap('round') # line cap

# move to horizontal center
translate(width()/2, 0)

# determine length of each line
myBranchHeight = 100

# define a function to draw a Y branch
# takes level as an argument
def myBranch(level=0):
    print(level)
    # vertical line
    line((0, 0), (0, myBranchHeight))
    # move to top of vertical line
    translate(0, myBranchHeight)

    # a list of angles to draw subsequent
    # lines at 
    myAngleList = [-30, 30]
    # if we are within our allowed levels
    # keep drawing other lines at an angle
    if level < 5:
        for myAngle in myAngleList:
            # save state so rotation is localized
            with savedState():
                rotate(myAngle)
                # instead of drawing line() again
                # call myBranch() from within itself
                # to make it recurisve
                # up the level number so we can keep
                # track of how deep we are
                #line((0, 0), (0, myBranchHeight))
                myBranch(level+1)

myBranch()