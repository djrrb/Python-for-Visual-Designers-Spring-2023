newPage(1000, 1000)
myX = 0
myStripeCount = 10
myStripeWidth = width()/myStripeCount
print('canvas', width(), height())
print('stripe count', myStripeCount)
print('stripe width', myStripeWidth)
for myStripeNumber in range(myStripeCount):
    print(myStripeNumber, myX)
    fill(random(), random(), random(), 1)
    #cmykFill(0, 1, 0, 0)
    rect(myX, 0, myStripeWidth, height())
    fontSize(100)
    #text('hello world', (myX, 0))
    
    myX = myX + myStripeWidth
    #image('/Users/david/Desktop/helloWorld.jpg', (myX, 0))


