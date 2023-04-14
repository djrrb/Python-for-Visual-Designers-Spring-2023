showHelperCode = True

# make a circle to fill the canvas
oval(0, 0, width(), height())

fill(1)
# we could position it manually
#oval(350, 350, 300, 300) # x, y, width, height

# or we position it systematically

# make a size variable to describe the center
myDonutHoleSize = 400

# to get the lower left
# we can start at the center
# and shift the shape half its size
# down and to the left
oval(
    width()/2 - myDonutHoleSize/2, 
    height()/2 - myDonutHoleSize/2, 
    myDonutHoleSize, 
    myDonutHoleSize
)

####
# the code below is just to help explain
# the positioning of the center circle

if showHelperCode:

    # draw a little blue circle to show where
    # center of canvas is


    fill(0, 0, 1)
    oval(
        width()/2-5,
        height()/2-5,
        10, 
        10
    )
    text('Center of canvas', (width()/2, height()/2-20), align="center")
    
    # draw a little red circle to show where
    # the lower left origin of the middle circle is

    
    fill(1, 0, 0)
    oval(
        width()/2 - myDonutHoleSize/2-5,
        height()/2 - myDonutHoleSize/2-5,
        10, 
        10
    )
    text(
        'Lower left of donut hole', 
        (
            width()/2 - myDonutHoleSize/2,
            height()/2 - myDonutHoleSize/2-20
        ), 
        align="center"
    )
    
saveImage('donutMarkup.png')
    