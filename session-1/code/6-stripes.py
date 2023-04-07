# make a new page
newPage(1000, 1000)

# define some variables
myX = 0 # where our X value should start
myStripeCount = 10 # how many stripes

# calculate the width of each stripe
# by taking the full width of the canvas
# and dividing it by the number of stripes
myStripeWidth = width()/myStripeCount

# print some basic info about our document
print('canvas', width(), height())
print('stripe count', myStripeCount)
print('stripe width', myStripeWidth)

# now loop through each stripe
# using range to generate a sequence of numbers between 0 and 9
for myStripeNumber in range(myStripeCount):
    # print the current stripe number and x value
    print(myStripeNumber, myX)
    # set the fill color to random
    fill(random(), random(), random())
    #cmykFill(0, 1, 0, 0)
    # draw a rectangle
    rect(myX, 0, myStripeWidth, height())
    # augment the myX value each time    
    myX = myX + myStripeWidth


