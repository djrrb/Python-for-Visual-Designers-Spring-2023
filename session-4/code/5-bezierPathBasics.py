# define a path
myPath = BezierPath()

# draw outlines into it
myPath.rect(0, 0, 100, 100)

# this is like “create outlines”
myPath.text('Hello world')

# draw the path to canvas
drawPath(myPath)