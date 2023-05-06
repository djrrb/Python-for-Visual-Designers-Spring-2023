# in this script we will draw vector items like text into an image
# once it is an ImageObject, we can run filters on it and stuff

myFrameCount = 24 # how many frames
myTwirlSize = 1 # starting twirl amount
# the direction of the animation
# start with 1 (numbers going up)
# then it will change to -1 (numbers going down)
direction = 1 

# there are two phases, up and down
for phase in range(2):
    # loop through each frame
    for myFrameNumber in range(myFrameCount):
        # make a new page
        newPage()
        frameDuration(1/24)
        # make a background
        fill(1)
        rect(0, 0, width(), height())
        # make an empty image object
        myImage = ImageObject()
        # draw text into the imageObject
        with myImage:
            fill(0)
            font('Comic Sans MS', 170)
            text('Hello world', (width()/2, height()/2), align="center")

        # run a filter on the image
        # use the myTwirlSize variable
        myImage.twirlDistortion(
            center=(width()/2, height()/2),
            radius=myTwirlSize
            )
        # augment the myTwirlSize variable
        # so that the next frame is different
        # multiply by direction so the numbers will get
        # bigger at first, and then will be negative
        # when direction is -1
        myTwirlSize += 20 * direction
        # draw the image to canvas
        image(myImage, (0, 0))
    # after the phase is over, change the direction
    direction = -1
# save the image
saveImage('twirl.gif')