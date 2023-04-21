# define an image
myImage = ImageObject('black-raspberries.jpg')

# get the color of a pixel
# given the image and the coordinates of the pixel
print( imagePixelColor(myImage, (570, 620)) )

# set that color to a variable
myColor = imagePixelColor(myImage, (570, 620))

# set the fill to myColor
# unpacking the rgba values
# and passing those individually
# rather as a single tuple
fill(*myColor)

# draw a rectangle the size of the canvas
# so we can see the color
rect(0, 0, width(), height())