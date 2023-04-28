myDie1 = randint(1, 6)
myDie2 = randint(1, 6)

myAttempts = 0

keepRolling = True

while keepRolling:
    myDie1 = randint(1, 6)
    myDie2 = randint(1, 6)
    print('Attempt', myAttempts, ':', myDie1, myDie2)
    if myDie1 == 1 and myDie2 == 1:
        keepRolling = False

    myAttempts += 1
    