# set some basic parameters
myShapeCount = 30
myPageCount = 10

# calculate the width of each stripe
myStripeWidth = width()/myShapeCount

# this is the range that we will loop through
print(list(range(myShapeCount)))

# this is a toggle variable
# we will change it from True to False
myToggle = False

# for item in sequence
for myPageNumber in range(myPageCount):
    # make a new page
    newPage()
    # reset x to 0, so that we always
    # start at the left side of the screen
    myX = 0
    # now loop through each shape
    for myShapeNumber in range(myShapeCount):
        # this is the code that repeats
        print(myShapeNumber)
        if myToggle:
            # if myToggle is True run this code
            # set the fill to a random color
            fill(random(), random(), random())
            # switch the toggle to False
            myToggle = False
        else:
            # if myToggle is False run this code
            # set fill to black
            fill(0)
            # switch myToggle back to True
            myToggle = True
        # draw our shape
        rect(myX, 0, myStripeWidth, height())
        # augment our X variable
        myX += myStripeWidth 
        # same as myX = myX + myStripeWidth

saveImage('ifStatementAlternatingColorAnimation.mp4')