myImage = ImageObject('black-raspberries.jpg')


#myImage.sepiaTone(1)
myImage.vignette(100, 0.5)
myImage.kaleidoscope(12)


print( myImage.size() )
newPage( * myImage.size()  )

image(myImage, (0, 0))

saveImage('fancy-berries.jpg')