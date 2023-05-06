def tooth():
    # draw one houndstooth pattern at 200 x 200
    # starting at (0, 0)
    bp = BezierPath()

    # bottom left triangle
    bp.moveTo((0, 0)) # bottom left corner
    bp.lineTo((50, 0)) # bottom edge
    bp.lineTo((0, 50)) # hypotenuse
    bp.closePath() # left edge
    
    # large shape
    bp.moveTo((0, 100)) # start middle left
    bp.lineTo((100, 0)) # down to center bottom
    bp.lineTo((100, 50)) # up a bit
    bp.lineTo((50, 100)) # diagonal to the left
    bp.lineTo((100, 100)) # horizontal up to the right
    bp.lineTo((100, 150)) # vertical up
    bp.lineTo((150, 100)) # diagonal down to the right
    bp.lineTo((200, 100)) # horizontal to the right middle
    bp.lineTo((100, 200)) # diagonal to the top center
    bp.lineTo((0, 200)) # horizontal to the upper left corner
    bp.closePath() # down the left edge

    bp.moveTo((200, 200)) # top right corner
    bp.lineTo((150, 200)) # horizontal to the left
    bp.lineTo((200, 150)) # diagonal down and to the right
    bp.closePath() # back up to the top right corner
    drawPath(bp)

# how many cols and rows
myColCount, myRowCount = 10, 10

# determine the cell size based on the canvas size
myCellWidth = width()/myColCount
myCellHeight = height()/myRowCount

# our swatch is drawn at 200x200
# so if we want to scale it to fit the cell, 
# we can divide cellSize/200
myXScale = myCellWidth/200
myYScale = myCellHeight/200

# loop through rows
for myRowNumber in range(myRowCount):
    # save state so we can return to the left edge
    with savedState():
        # loop through columns
        for myColNumber in range(myColCount):
            # make another savedState() so that the
            # scale only affects our houndstooth swatch
            # and not the rest of the grid
            with savedState():
                scale(myXScale, myYScale)
                tooth()
            # exit saved state
            # moved to the right to draw the next column
            translate(myCellWidth)
        # exit saved state
    # move up to draw the next row
    translate(0, myCellHeight)
            
# draw a second page to see one pattern swatch
newPage(200, 200)
tooth()
