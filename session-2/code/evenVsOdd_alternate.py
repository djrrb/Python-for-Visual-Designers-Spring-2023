# another way to calculate even vs odd

# if a number / 2 is equivalent to the the number / 2 converted to an integer, then it is even

# pick a number
myNumber = 11


print(myNumber, myNumber/2, int(myNumber/2))

if myNumber / 2 == int(myNumber / 2):
    print('this is even!')
else:
    print('this is odd!')
    