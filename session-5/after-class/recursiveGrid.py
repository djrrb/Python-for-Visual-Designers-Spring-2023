def grid(size=1000, level=0):
    # each grid has a saved state so it only
    # affects the other grids inside it
    with savedState():
        # determine how many rows or columns are in this grid
        rows = cols = randint(1, 3)
        # figure out how big each cell is
        cellSize = size/rows
        
        # make my grid
        for row in range(rows):
            with savedState():
                for col in range(cols):
                    
                    # if we are less than 3 levels deep
                    # set the fill to a random color
                    # but rather than drawing a shape
                    # create a new grid
                    if level < 3:
                        fill(random(), random(), random())
                        grid(cellSize, level+1)
                    # if we are more than 3 levels deep
                    # draw an oval to end the recursion
                    else:
                        oval(0, 0, cellSize, cellSize)
                    # move one column to the right
                    translate(cellSize)
                # exit the saved state to return to
                # the left side of the page
            # move one row up
            translate(0, cellSize)
            
# draw five pages
pages = 5
for page in range(pages):
    newPage()
    fill(1)
    rect(0, 0, width(), height())
    grid(width())
    saveImage('recursiveGrid'+str(page)+'.png')
