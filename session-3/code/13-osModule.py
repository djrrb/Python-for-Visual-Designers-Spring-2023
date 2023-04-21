# make 100 folders

# import the os module
import os

# loop 100 times
for myNumber in range(100):
    # make a new directory
    os.mkdir('my new directory '+str(myNumber))