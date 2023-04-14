# define some constants
myRowCount = 10
myColCount = 10

# calculate the cell width and height
myCellWidth = width()/myColCount
myCellHeight = height()/myRowCount

print(myCellWidth, myCellHeight)

# this time we will always draw the shape at (0, 0)
# but we will use translate to move the location of (0, 0) as we go

# loop through the rows
for myRowNumber in range(myRowCount):
    # we want to be able to return to the left of the screen
    # so save the state
    with savedState():
        # loop through the columns
        for myColNumber in range(myColCount):
            # draw our shape at (0, 0)
            oval(0, 0, myCellWidth, myCellHeight)
            # move us to the right
            translate(myCellWidth, 0)
            # this runs once per column
        # this ends the column loop
    # this exits the saved state
    # and we undo all of that rightward movement
    # now move us up to the next row
    translate(0, myCellHeight)