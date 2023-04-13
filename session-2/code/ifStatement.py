myShapeCount = 10
print(list(range(myShapeCount)))
# for item in sequence
myX = 0
myToggle = False
for myShapeNumber in range(myShapeCount):
    # this is the code that repeats
    print(myShapeNumber)
    fill(random(), random(), random())
    if myToggle:
        rect(myX, 0, 100, height())
        myToggle = False
    else:
        oval(myX, 0, 100, height())
        myToggle = True
    myX += 100 # myX = myX + 100
print('done')