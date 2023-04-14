# define some constants
myRowCount = 10
myColCount = 10
# calculate the dimensions of each cell
myCellHeight = height()/myRowCount
myCellWidth = width()/myColCount

# loop through the rows
for myRowNumber in range(myRowCount):
    print('this runs once per row')
    # loop through the columns within each row
    for myColNumber in range(myColCount):
        print('\tthis is cell row', myRowNumber, 'col', myColNumber)
        # draw an oval
        # the x is offset by the col number times the cell width
        # the y is offset by the row number times the cell height
        oval(
            myColNumber*myCellWidth,  # x offset
            myRowNumber*myCellHeight, # y offset
            myCellWidth, # width
            myCellHeight # height
        )