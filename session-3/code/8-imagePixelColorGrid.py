# define an image object
myImage = ImageObject('black-raspberries.jpg')

# set the canvas dimensions to the image size
# unpacking the width and height to pass directly to newPage()
newPage(*myImage.size())

# how many rows and columns
myYCount, myXCount = 50, 50

# determine the cell dimensions
myCellHeight = height()/myYCount
myCellWidth = width()/myXCount
print('cell width', myCellWidth)

# loop through rows
for myYNumber in range(myYCount):
    print('this is a new row')
    # loop through columns 
    for myXNumber in range(myXCount):
        print('\tthis is a new cell', myXNumber, myXNumber*myCellWidth)
        # determine x and y position of cell
        myX = myXNumber*myCellWidth
        myY = myYNumber*myCellHeight
        # eyedrop the image at that position
        myColor = imagePixelColor(myImage, (myX, myY))
        # set the fill color to our eyedropped color
        # unpacking the rgba values
        fill(*myColor)
        # draw a shape, either oval or rectangle
        if random() > .3:
            oval(myX, myY, myCellWidth, myCellHeight)
        else:
            rect(myX, myY, myCellWidth, myCellHeight)