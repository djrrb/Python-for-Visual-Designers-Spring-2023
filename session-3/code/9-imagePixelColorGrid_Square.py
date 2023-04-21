# define an image
myImage = ImageObject('black-raspberries.jpg')
# get the image width and height as variables
myImageWidth, myImageHeight = myImage.size()

# how big do we want each cell to be
myCellHeight = 50
myCellWidth = 50

# determine the number of whole cells that can fit into the image
# convert that number to an integer

myXCount = int(myImageWidth//myCellWidth)
myYCount = int(myImageHeight//myCellHeight)
print(width(), height())
print(myXCount, myYCount)

# draw a newPage with dimensions based on the
# cells we are going to draw
newPage(myXCount*myCellWidth, myYCount*myCellHeight)

print('cell width', myCellWidth)

# draw the grid
# loop through rows
for myYNumber in range(myYCount):
    print('this is a new row')
    # loop through cols
    for myXNumber in range(myXCount):
        print('\tthis is a new cell', myXNumber, myXNumber*myCellWidth)
        # calculate x and y
        myX = myXNumber*myCellWidth
        myY = myYNumber*myCellHeight
        # do the eydropper on the image at our x and y
        myColor = imagePixelColor(myImage, (myX, myY))
        print(myColor)
        # set the fill, unpacking the rgba elements
        # of the color
        fill(*myColor)
        
        # draw an oval or rectangle
        if random() > .3:
            oval(myX, myY, myCellWidth, myCellHeight)
        else:
            rect(myXNumber*myCellWidth, myYNumber*myCellHeight, myCellWidth, myCellHeight) 