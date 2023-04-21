# import the choice function from the random library
from random import choice

# determine the grid 
myColCount, myRowCount = 10, 10
# get the dimensions of each cell
myCellWidth = width()/myColCount
myCellHeight = height()/myRowCount

# the alphabet, to give us letters to choose from
myAlphabet = 'abcdefghijklmnopqrstuvwxyz'

# make the grid, loop through rows
for myRowNumber in range(myRowCount):
    # and loop through columns
    for myColNumber in range(myColCount):
        # get the x and y coordinates
        # myColNumber * myCellWidth gives us the bottom left of cell
        # adding myCellWidth/2 gets us the middle of the cell
        myX = myColNumber * myCellWidth + myCellWidth/2
        myY = myRowNumber * myCellHeight + myCellHeight/2
        
        # set the font and font size
        font('Comic Sans MS')
        fontSize(100)
        
        # choose a random letter from the alphabert
        myLetter = choice(myAlphabet)
        
        #get the dimensions of that text with that font at that size
        myTextWidth, myTextHeight = textSize(myLetter)
        print(myTextWidth)
        
        # draw a blue box corresponding to the letter width
        fill(0, 1, 1)
        rect(
            myX-myTextWidth/2, 
            myY-fontXHeight()/2, 
            myTextWidth, 
            50
        )
        # set the fill to black
        fill(0)
        # draw the letter
        text(
            myLetter, 
            (myX, myY-fontXHeight()/2), # lower it by half 
            # the x-height to vertically center
            align="center" # horizontally aligned to center
        )
        
        # draw helper shapes to help us see the grid and the center of the cell
        with savedState():
            fill(1, 0, 0)
            oval(myX-5, myY-5, 10, 10)
            fill(None)
            stroke(1, 0, 0)
            rect(myX-myCellWidth/2, myY-myCellHeight/2, myCellWidth, myCellHeight)
