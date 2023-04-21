myImage = ImageObject('black-raspberries.jpg')

print( imagePixelColor(myImage, (0, 0)) )

myColor = imagePixelColor(myImage, (570, 620))


fill(*myColor)

rect(0, 0, width(), height())