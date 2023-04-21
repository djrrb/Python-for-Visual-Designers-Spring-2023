myImage = ImageObject('black-raspberries.jpg')
print( myImage.size() )

newPage( * myImage.size()  )

image(myImage, (0, 0))