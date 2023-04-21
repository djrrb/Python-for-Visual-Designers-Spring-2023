# how many pages to draw
myPageCount = 10
# determine how many points we want our shape to have
myCornerCount = 50

# loop through the pages
for myPageNumber in range(myPageCount):
    # make a new page
    newPage()
    
    # make an empty list
    myPointList = []

    # loop through myCornerCount
    for myCornerNumber in range(myCornerCount):
        # deterine a random X and Y point
        # between 0 and the canvas dimensions
        myX = randint(0, width())
        myY = randint(0, height())
        # append our X, Y as a tuple to myPointList
        myPointList.append((myX, myY))
    
    # draw a polygon using the list of points
    # we need to unpack the list
    # so that the polygon() function receives all of the (x, y) tuples directly, rather than a single list
    polygon(*myPointList)
    
saveImage('randomPolygon.gif')