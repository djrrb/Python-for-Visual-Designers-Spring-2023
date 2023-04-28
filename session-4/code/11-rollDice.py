# roll dice until we get snake eyes

# keep track of number of attempts
myAttempts = 0

# this variable determines whether we should keep trying
# once we 
keepRolling = True

# as long as keepRolling is True, run the loop
while keepRolling:
    # roll a pair of dice
    myDie1 = randint(1, 6)
    myDie2 = randint(1, 6)
    # keep track of our number of attempts by augmenting the variable
    myAttempts += 1

    # print the results
    print('Attempt', myAttempts, ':', myDie1, myDie2)
    # if both dice are 1, we have snake eyes
    # and we can stop rolling
    if myDie1 == 1 and myDie2 == 1:
        keepRolling = False
