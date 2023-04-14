# // gives us whole number division
#print(5//2)
# % gives us the remainder
#print(5 % 2)

# x % 2 will be 1 for odd numbers
# and 0 for even numbers

# so we can do odd/even without a toggle
myX = 0
for myNumber in range(10):
    print(myNumber, myNumber % 2)
    if myNumber % 2:
        # number has a remainder and is odd
        rect(myX, 0, 100, height())
    else:
        # number has a remainder and is even
        oval(myX, 0, 100, height())
    myX += 100