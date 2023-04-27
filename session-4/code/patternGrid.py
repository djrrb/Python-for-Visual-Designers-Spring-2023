# draw grid
myXCount, myYCount = 3, 3

myCellWidth = width()/myXCount
myCellHeight = height()/myYCount

newPage(1000, 1000)

# here’s where i define the swatch
def myPatternSwatch():
    with savedState():
        oval(0, 0, myCellWidth, myCellHeight)
        fill(1, 0, 0)
        fontSize(30)
        text('swatch!', (0, 0))
        stroke(0, 0, 1)
        strokeWidth(10)
        line((0, myCellHeight), (myCellWidth, 0))
        line((0, 0), (myCellWidth, myCellHeight))

# here’s where i repeat it

# loop across rows
for myYNumber in range(myYCount):
    # code here happens once per row
    # loop across columns
    with savedState():
        for myXNumber in range(myXCount):
            # code here happens once per cell
            print(myYNumber, myXNumber)
            fill(random(), random(), random())
            # draw a rectangle for each cell
            #rect(0, 0, myCellWidth, myCellHeight)
            # replace a rectangle with a different swatch
            myPatternSwatch()
            translate(myCellWidth, 0) # move to the right
    translate(0, myCellHeight) # move up


