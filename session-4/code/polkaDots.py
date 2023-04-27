myPageCount = 20

def centerOval(myW, myH):
    oval(-myW/2, -myH/2, myW, myH)

    
# set some variables
myRowCount = 40 # number of rows
myColCount = 40 # number of cols
myColWidth = width()/myRowCount # width of each col
myRowHeight = height()/myRowCount # width of each row
myBasicShapeSize = myColWidth*.75 # drw the shape at 3/4 the grid size, give or take
mySizeVariation = myBasicShapeSize // 10 # vary each shape randomly by 10%
# use two divide symbols so the result is an integer, which is required by the randint() function

myPageCount = 5

for myPageNumber in range(myPageCount):
    newPage()
    # make a pink background
    fill(0, 0, 0)
    rect(0, 0, width(), height())

    # set the fill color to brandom
    myRandomColor = random(), random(), random()

    # move to the center of each grid cell
    translate(myColWidth/2, myRowHeight/2)


    # loop through rows
    for myRowNumber in range(myRowCount):
        


        # save the state
        with savedState():
            for myColNumber in range(myColCount):
                
                
                
                # get a number between -mySizeVariation and mySizeVariation
                myVariationAmount = randint(-mySizeVariation, mySizeVariation)
                # get the size from the basic size and random variation
                myShapeSize = myBasicShapeSize + myVariationAmount
                # draw the oval
                if 25 > myColNumber > 15 and 25 > myRowNumber > 15:
                    fill(1)
                else:
                    fill(*myRandomColor)
                centerOval(myShapeSize, myShapeSize)
                # move to the right
                translate(myColWidth)
            # exit col loop
        # exit saved state
        # move up for each column
        translate(0, myRowHeight)


# exit all loops
saveImage('polkaDotPatternRandom.mp4')