# get an empty formatted string with some basic settings
myString = FormattedString(fontSize=30, lineHeight=40)

# loop through each font in my font
# enumerate() will also assign each font a number
for myNumber, myFont in enumerate(installedFonts()):
    # skip all system fonts that start with '.'
    if myFont.startswith('.'):
        continue
    # append our new font to the string
    myString.append(
        myFont+' ', 
        font=myFont, 
        fill=(random(), random(), random())
    ) 
    # max out after 500
    if myNumber > 500:
        break
        
# set a margin
myMargin = 50

# while there are still contents in myString
# keep adding new pages
# once myString is empty, stop the loop
while myString:
    # add new page
    newPage()
    # draw myString to the textBox, returning the overflow text
    # redefining myString with the overflow text whittles the
    # of myString down until there is nothing left
    myString = textBox(myString, (myMargin, myMargin, width()-myMargin*2, height()-myMargin*2))
    # print what is left to the console
    print(myString)

