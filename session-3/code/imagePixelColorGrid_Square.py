myImage = ImageObject('black-raspberries.jpg')
myImageWidth, myImageHeight = myImage.size()
print(myImage.size())
#newPage(*myImage.size())

# myColor = imagePixelColor(myImage, (570, 620))


# fill(*myColor)

# rect(0, 0, width(), height())


myCellHeight = 50
myCellWidth = 50

myXCount = int(myImageWidth//myCellWidth)
myYCount = int(myImageHeight//myCellHeight)
print(width(), height())
print(myXCount, myYCount)

newPage(myXCount*myCellWidth, myYCount*myCellHeight)

print('cell width', myCellWidth)

for myYNumber in range(myYCount):
    print('this is a new row')
    for myXNumber in range(myXCount):
        print('\tthis is a new cell', myXNumber, myXNumber*myCellWidth)
        myX = myXNumber*myCellWidth
        myY = myYNumber*myCellHeight
        myColor = imagePixelColor(myImage, (myX, myY))
        print(myColor)
        fill(*myColor)
        if random() > .3:
            oval(myX, myY, myCellWidth, myCellHeight)
        else:
            rect(myXNumber*myCellWidth, myYNumber*myCellHeight, myCellWidth, myCellHeight) 