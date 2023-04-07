# an example of drawing stripes manually

# make a new page
newPage('Letter')
# draw a rect with the default fill color
rect(0, 0, 100, height())
# set the fill to red
fill(1, 0, 0)
# draw the same rect but 100 units to the right
rect(100, 0, 100, height())
# set the fill to green
fill(53/255, 170/255, 61/255)
# draw the same rect but 100 units to the right
rect(200, 0, 100, height())
# set the fill to teal
fill(23/255, 120/255, 123/255)
# draw the same rect but 100 units to the right
rect(300, 0, 100, height())

# and so on and so forth

# better to do this with a loop!