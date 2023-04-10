# how many shapes should I draw?
myShapeCount = 100
# loop through the range between 0 and myShapeCount
for myNumber in range(myShapeCount):
    # set the fill color to a random semitransparent color
    # by setting the red value to 0, all the colors will be “cool”
    fill(
        0, # red value
        random(), # green value
        random(), # blue value
        .5 # alpha
    )
    # draw an oval anchored at the bottom lefthand corner
    # with a width and height that is a random value between 0
    # and the canvas width and height
    # random() is a number between 0 and 1
    # width() and height() are the dimensions of the canvas
    oval(
        0, # x position
        0, # y position
        random()*width(), # width value
        random()*height() # height value
    )