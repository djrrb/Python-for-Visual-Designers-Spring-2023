from random import choice

myFileName = 'myWords.txt'

with open(myFileName, encoding='utf-8') as myFile:
    myLines = myFile.readlines()
    print(myLines)


myCols = 10
myRows = 10
myCellWidth = 100
myCellHeight = 100

for myRow in range(myRows):
    for myCol in range(myCols):
        print(choice(myLines).strip())
        myString = choice(myLines).strip()
        myX = myCol * myCellWidth
        myY = myRow * myCellHeight
        font('Comic Sans MS', 16)
        text(myString, (myX, myY))