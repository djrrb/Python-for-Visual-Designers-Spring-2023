myFrames = 10
myX = 0
myXAdvance = width()/myFrames
print(myXAdvance)
for myFrame in range(myFrames):
    oval(myX, 100, 100, 100)
    myX += myXAdvance