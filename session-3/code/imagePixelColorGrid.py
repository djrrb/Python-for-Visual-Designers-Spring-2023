myImage = ImageObject('black-raspberries.jpg')

newPage(*myImage.size())

# myColor = imagePixelColor(myImage, (570, 620))


# fill(*myColor)

# rect(0, 0, width(), height())

myYCount, myXCount = 50, 50

myCellHeight = height()/myYCount
myCellWidth = width()/myXCount
print('cell width', myCellWidth)

for myYNumber in range(myYCount):
    print('this is a new row')
    for myXNumber in range(myXCount):
        print('\tthis is a new cell', myXNumber, myXNumber*myCellWidth)
        myX = myXNumber*myCellWidth
        myY = myYNumber*myCellHeight
        myColor = imagePixelColor(myImage, (myX, myY))
        fill(*myColor)
        if random() > .3:
            oval(myX, myY, myCellWidth, myCellHeight)
        else:
            rect(myXNumber*myCellWidth, myYNumber*myCellHeight, myCellWidth, myCellHeight) 