myShapeCount = 10
myPageCount = 10
print(list(range(myShapeCount)))
# for item in sequence

myToggle = False

for myPageNumber in range(myPageCount):
    newPage()
    myX = 0
    for myShapeNumber in range(myShapeCount):
        # this is the code that repeats
        print(myShapeNumber)
        if myToggle:
            fill(random(), random(), random())
            myToggle = False
        else:
            fill(0)
            myToggle = True
        rect(myX, 0, 100, height())
        myX += 100 # myX = myX + 100

saveImage('ifStatementAlternatingColorAnimation.mp4')