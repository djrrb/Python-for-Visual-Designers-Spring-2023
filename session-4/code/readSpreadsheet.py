import csv

myInch = 72
myMargin = 12

with open('Business Cards - Sheet1.csv', encoding='utf-8') as myFile:
    myCSV = csv.reader(myFile)
    for myRowNumber, myRow in enumerate(myCSV):
        if myRowNumber == 0:
            continue
        print(myRow[0])
        newPage(3.5*myInch, 2*myInch)
        
        font('Times', 15)
        #rect(100, 10, 141, 120)
        #rect(width()/3, myMargin, width()*2/3-myMargin, height()-myMargin*2)
        textBox(myRow[0], (width()/3, myMargin, width()*2/3-myMargin, height()-myMargin*2))
        
        with savedState():
            translate(10, 47)
            scale(.4)
            image('https://universityinnovation.org/images/5/5c/Cooper_union_logo.png', (myMargin, myMargin))
            
        text('hello world', (0, 0))