from random import choice
with open('myWordList.txt') as myFile:
    myWordList = myFile.readlines()

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
        myX = myXNumber*myCellWidth
        myY = myYNumber*myCellHeight
        rect(myX, myY, 10, myCellHeight)
        rect(myX+15, myY, 10, myCellHeight)
        rect(myX, myY, myCellWidth, 10)
        rect(myX, myY+15, myCellWidth, 10)
        fill(0)
        fontSize(15)
        text(choice(myWordList), (myX+25, myY+45))
        #oval(myXNumber*myCellWidth, myYNumber*myCellHeight, myCellWidth, myCellHeight)
