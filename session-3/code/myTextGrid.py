from random import choice

myColCount, myRowCount = 10, 10
myCellWidth = width()/myColCount
myCellHeight = height()/myRowCount

myAlphabet = 'abcdefghijklmnopqrstuvwxyz'

for myRowNumber in range(myRowCount):
    for myColNumber in range(myColCount):
        myX = myColNumber * myCellWidth + myCellWidth/2
        myY = myRowNumber * myCellHeight + myCellHeight/2
        font('Comic Sans MS')
        fontSize(100)
        myLetter = choice(myAlphabet)
        
        myTextWidth, myTextHeight = textSize(myLetter)
        print(myTextWidth)
        fill(0, 1, 1)
        rect(myX-myTextWidth/2, myY-fontXHeight()/2, myTextWidth, 50)
        fill(0)
        
        text(myLetter, (myX, myY-fontXHeight()/2), align="center" )
        with savedState():
            fill(1, 0, 0)
            oval(myX-5, myY-5, 10, 10)
            fill(None)
            stroke(1, 0, 0)
            rect(myX-myCellWidth/2, myY-myCellHeight/2, myCellWidth, myCellHeight)
