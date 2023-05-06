# make a rectangle
myRectangle = BezierPath()
myRectangle.rect(100, 100, 250, 250)

# make a circle
myCircle = BezierPath()
myCircle.oval(200, 200, 250, 250)

# draw them
newPage()
drawPath(myRectangle)
newPage()
drawPath(myCircle)

# intersect them
newPage()
intersectionPath = myRectangle.intersection(myCircle)
drawPath(intersectionPath)

# unite them
newPage()
unionPath = myRectangle.union(myCircle)
drawPath(unionPath)

# subtract one from the other
newPage()
differencePath = myRectangle.difference(myCircle)
drawPath(differencePath)

# draw the xor (the opposite of union)
newPage()
xorPath = myRectangle.xor(myCircle)
drawPath(xorPath)