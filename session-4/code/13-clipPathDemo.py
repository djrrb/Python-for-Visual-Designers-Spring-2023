# define a triangle centered at (0, 0)
def myTriangle():
    polygon(
        (-50, -50),
        (0, 50),
        (50, -50)
        )
        
# define some text with formatting 
# as a FormattedString() object
myText = FormattedString('Hi', fontSize=990, font='Comic Sans MS')
       
# how many shapes to draw 
myShapeCount = 300
        
# define an empty bezier path
myPath = BezierPath()
# feed our text into the bezierPath to convert
# the text to outlines
myPath.text(myText)

# add a bottom margin
translate(0, 100)

# add a blend mode if we want
blendMode('overlay')

# we are about to do a clipping path
# but save our state so we can easily exit
# the clipping path
with savedState():
    # create a clipping path so that anything we draw to canvas will only appear within myPath
    clipPath(myPath)
        
    # draw a bunch of shapes
    for myShapeNumber in range(myShapeCount):
        # since our triangle is based around (0, 0)
        # we can temporary move (0, 0) to random points on the canvas
        # and then use the savedState() to always return to the lower left
        
        # move (0, 0) to a random point
        with savedState():
            # get an x and y value that are
            # random values between 0 and 
            # the canvas dimensions
            myX = randint(0, width())
            myY = randint(0, height())
            # move (0, 0) to that random point
            translate(myX, myY)
            # do some other canvas transformations
            rotate(randint(-10, 10))
            skew(randint(-10, 10))
            fill(random(), random(), 0)
            # draw our shape
            myTriangle()
            
# change the blend mode so that this text draws over
blendMode('normal')
# draw some text
fontSize(30)
text('Hello there', (140, 0))