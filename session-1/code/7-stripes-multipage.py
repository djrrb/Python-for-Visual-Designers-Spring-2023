# define some variables
myPageCount = 10 # how many pages
myStripeCount = 10 # how many stripes

# calculate the width of each stripe
# by taking the full width of the canvas
# and dividing it by the number of stripes
myStripeWidth = width()/myStripeCount

# print some basic info about our document
print('canvas', width(), height())
print('stripe count', myStripeCount)
print('stripe width', myStripeWidth)

# loop through each page
for myPageNumber in range(myPageCount):
    # for each page, print the page number
    print('PAGE', myPageNumber)
    # make a new page
    newPage(1000, 1000)
    # reset myX to 0, so that
    # we always start on the left side of the pages
    myX = 0

    # now loop through each stripe
    for myStripeNumber in range(myStripeCount):
        # print the stripe number
        print(myStripeNumber, myX)
        # set the fill to a random color
        fill(random(), random(), random(), 1)
        # draw a rectangle at myX
        # using the myStripeWidth variable for the width
        # and the full canvas height
        rect(myX, 0, myStripeWidth, height())

        # now let’s augment the myX variable
        # adding the stripeWidth value each time
        # so that it keeps getting bigger
        # 0, 100, 200, 300, etc...
        myX = myX + myStripeWidth

# at the end, save the file
# in a PDF, pages are pages
# in a GIF or MP4, pages are frames in an animation
saveImage('animatedStripes.gif')