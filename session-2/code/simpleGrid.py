myRowCount = 10
myColCount = 10

myCellHeight = height()/myRowCount
myCellWidth = width()/myColCount

for myRowNumber in range(myRowCount):
    print('this runs once per row')
    for myColNumber in range(myColCount):
        #print('\tthis runs once per column per row')
        print('\tthis is cell', myRowNumber, myColNumber)
        oval(
            myColNumber*myCellWidth,  # x offset
            myRowNumber*myCellHeight, # y offset
            myCellWidth, # width
            myCellHeight # height
        )