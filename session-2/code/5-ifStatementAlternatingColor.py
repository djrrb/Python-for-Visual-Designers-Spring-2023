myShapeCount = 10
print(list(range(myShapeCount)))
# for item in sequence
myX = 0
myToggle = False
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
print('done')