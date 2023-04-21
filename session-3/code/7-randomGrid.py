# define the number of rows and cols 
myYCount = 10
myXCount = 10

# determine dimensions of each cell
myCellHeight = height()/myYCount
myCellWidth = width()/myXCount

# loop through each row
for myYNumber in range(myYCount):
    print('this is a new row')
    # loop through each cell
    for myXNumber in range(myXCount):
        print('\tthis is a new cell', myXNumber, myXNumber*myCellWidth)
        # set a random fill color
        fill(random(), random(), random())
        # random() will be a number between 0 and 1
        # we can use an if statement to make something happen
        # a certain percentage of the time, randomly
        if random() > .3:
            # draw an oval if random > .3 (70% of the time)
            oval(
                myXNumber*myCellWidth, 
                myYNumber*myCellHeight, 
                myCellWidth, 
                myCellHeight
            )
        else:
            # draw an square otherwise (30% of the time)
            rect(
                myXNumber*myCellWidth, 
                myYNumber*myCellHeight, 
                myCellWidth, 
                myCellHeight
            ) 