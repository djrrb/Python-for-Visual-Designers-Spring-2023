myRowCount = 10
myColCount = 10

myCellWidth = width()/myColCount
myCellHeight = height()/myRowCount

print(myCellWidth, myCellHeight)
#newPage(5000, 1000)
for myRowNumber in range(myRowCount):
    with savedState():
        for myColNumber in range(myColCount):
            oval(0, 0, myCellWidth, myCellHeight)
            translate(myCellWidth, 0)
            # this runs once per column
        # this ends the column loop
    # this exits the saved state
    # and we undo all of that rightward movement
    translate(0, myCellHeight)