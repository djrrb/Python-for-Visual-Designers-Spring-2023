from random import choice
myWords = ['apple', 'orange', 'banana', 'asasdf']


# with open('/usr/share/dict/words') as myFile:
#     myWords = myFile.readlines()
    

myPoem = ''

for myNumber in range(25):
    myPoem += choice(myWords).strip() + ' '
    
print(myPoem)
