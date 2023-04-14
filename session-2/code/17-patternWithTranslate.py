myRowCount = 10
myColCount = 10

myCellWidth = width()/myColCount
myCellHeight = height()/myRowCount

# make a custom function with some stuff
def myPatternElement():
    # let’s undo all canvas transformations
    # within the function with a savedState
    # this way the function is nondestructive
    with savedState():
        rect(0, 0, myCellWidth/2, myCellHeight/2)
        fill(1, 0, 0)
        #polygon((20, 20), (50, 50), (-40, 30))
        oval(
            myCellWidth/3, 
            myCellHeight/3, 
            myCellWidth/2, 
            myCellHeight/2
        )
        oval(
            myCellWidth*.75, 
            myCellHeight*.75, 
            myCellWidth/4, 
            myCellHeight/4
        )

print(myCellWidth, myCellHeight)

# make a grid
for myRowNumber in range(myRowCount):
    with savedState():
        for myColNumber in range(myColCount):
            # rather than drawing a shape
            # call our special function
            myPatternElement()
            # move to the right
            translate(myCellWidth, 0)
    

            # this runs once per column
        # this ends the column loop
    # this exits the saved state
    # and we undo all of that rightward movement
    translate(0, myCellHeight)
    
