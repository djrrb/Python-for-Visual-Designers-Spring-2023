#print(5//2)
#print(5 % 2)

myX = 0
for myNumber in range(10):
    print(myNumber, myNumber % 2)
    if myNumber % 2:
        rect(myX, 0, 100, height())
    else:
        oval(myX, 0, 100, height())
    myX += 100