stroke(0)
strokeWidth(10)
lineCap('round')
#line((0, 0), (100, 100))

myLineCount = 500

for myLineNumber in range(myLineCount):
    
    myX1 = randint(0, width())
    myX2 = randint(0, width())
    myY1 = randint(0, height())
    myY2 = randint(0, height())
    stroke(random(), random(), random())
    
    line((myX1, myY1), (myX2, myY2))