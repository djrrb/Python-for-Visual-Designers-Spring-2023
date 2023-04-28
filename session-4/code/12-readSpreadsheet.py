# import the CSV library
import csv

myInch = 72 # 72 points in an inch
myMargin = 12 # margin size

# open the CSV file and define a variable
# myFile to represent the file
with open('Business Cards - Sheet1.csv', encoding='utf-8') as myFile:
    # read the file as a CSV
    myCSV = csv.reader(myFile)
    # loop through the rows in a CSV
    # assigning each row a number with enumerate()
    for myRowNumber, myRow in enumerate(myCSV):
        # skip the first row since it’s headers
        if myRowNumber == 0:
            continue
        # print the name
        print(myRow[0])
        
        # make a business card
        newPage(3.5*myInch, 2*myInch)
        
        # do some formatting
        font('Times', 15)
        #rect(100, 10, 141, 120)
        #rect(width()/3, myMargin, width()*2/3-myMargin, height()-myMargin*2)
        textBox(myRow[0], (width()/3, myMargin, width()*2/3-myMargin, height()-myMargin*2))
        
        # draw an image with some formatting
        # that is only available for that image
        with savedState():
            translate(10, 47)
            scale(.4)
            image('https://universityinnovation.org/images/5/5c/Cooper_union_logo.png', (myMargin, myMargin))
            
        # exit the savedState to keep drawing text 
        text('hello world', (0, 0))