myFrames = 10
myX = 0
# how far to the right do we move with each frame
myXAdvance = width()/myFrames
print(myXAdvance)
# loop through frames
for myFrame in range(myFrames):
    # draw one circle per page
    newPage()
    # draw oval
    oval(myX, 100, 100, 100)
    # augment to move the x value to the right
    myX += myXAdvance