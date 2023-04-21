myImage = ImageObject('black-raspberries.jpg')

# myColor = imagePixelColor(myImage, (570, 620))


# fill(*myColor)

# rect(0, 0, width(), height())

myYCount = 10
myXCount = 10

myCellHeight = height()/myYCount
myCellWidth = width()/myXCount
print('cell width', myCellWidth)

for myYNumber in range(myYCount):
    print('this is a new row')
    for myXNumber in range(myXCount):
        print('\tthis is a new cell', myXNumber, myXNumber*myCellWidth)
        fill(random(), random(), random())
        if random() > .3:
            oval(myXNumber*myCellWidth, myYNumber*myCellHeight, myCellWidth, myCellHeight)
        else:
            rect(myXNumber*myCellWidth, myYNumber*myCellHeight, myCellWidth, myCellHeight) 