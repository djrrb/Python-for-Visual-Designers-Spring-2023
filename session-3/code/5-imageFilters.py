# define an image object
myImage = ImageObject('black-raspberries.jpg')

# manipulate this imageObject using its methods
# https://drawbot.com/content/image/imageObject.html
myImage.sepiaTone(1)
myImage.vignette(100, 0.5)
myImage.kaleidoscope(12)

# get the size of the image
print( myImage.size() )

# set the canvas size to equal the image size
# unpacking width and height from the tuple
# and feeding them separately to newPage()
newPage( * myImage.size()  )

# draw the image object to the canvas at (0, 0)
image(myImage, (0, 0))

# save our new image
saveImage('fancy-berries.jpg')