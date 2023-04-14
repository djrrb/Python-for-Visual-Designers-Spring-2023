# a basic if statement
myShapeCount = 10

# for item in sequence
myX = 0

# our toggle variable will switch
# between True and False
myToggle = False

# loop through shapes, for item in sequence
for myShapeNumber in range(myShapeCount):
    # this is the code that repeats
    print(myShapeNumber)
    # set the color
    fill(random(), random(), random())
    if myToggle:
        # if myToggle is True, run this code
        rect(myX, 0, 100, height())
        # switch myToggle to false
        # so next time will be different
        myToggle = False
    else:
        # if myToggle is False, run this code
        oval(myX, 0, 100, height())
        # switch myToggle to true
        # so next time will be different
        myToggle = True
    # move the next shape to the right
    myX += 100 # myX = myX + 100
print('done')