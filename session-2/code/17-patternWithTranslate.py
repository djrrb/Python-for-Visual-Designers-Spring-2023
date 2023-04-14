myRowCount = 10
myColCount = 10

myCellWidth = width()/myColCount
myCellHeight = height()/myRowCount

def myPatternElement():
    with savedState():
        rect(0, 0, myCellWidth/2, myCellHeight/2)
        fill(1, 0, 0)
        #polygon((20, 20), (50, 50), (-40, 30))
        oval(myCellWidth/2, myCellHeight/2, myCellWidth, myCellHeight)

#def myPatternElement():
#    image('myPatternElement.pdf', (0, 0))

print(myCellWidth, myCellHeight)
#newPage(5000, 1000)
for myRowNumber in range(myRowCount):
    with savedState():
        for myColNumber in range(myColCount):
            myPatternElement()
            translate(myCellWidth, 0)
    
            myCellWidth -= 5
            # this runs once per column
        # this ends the column loop
    # this exits the saved state
    # and we undo all of that rightward movement
    translate(0, myCellHeight)
    
saveImage('blah.svg')