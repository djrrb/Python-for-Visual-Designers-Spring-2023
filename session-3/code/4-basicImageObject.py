# make an image object
# this gives us space between when we define the image
# and when we draw it to the canvas

# define an image
myImage = ImageObject('black-raspberries.jpg')

# get its size
print( myImage.size() )

# set the canvas size to equal the image size
# unpacking width and height from the tuple
# and feeding them separately to newPage()
newPage( * myImage.size()  )

# draw the image to the canvas
image(myImage, (0, 0))