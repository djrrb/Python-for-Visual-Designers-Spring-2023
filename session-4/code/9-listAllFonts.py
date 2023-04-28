# get an empty formatted string with some basic settings
myString = FormattedString(fontSize=25, lineHeight=40)

# loop through each font in my font
# enumerate() will also assign each font a number
for myNumber, myFont in enumerate(installedFonts()):
    # skip all system fonts that start with '.'
    if myFont.startswith('.'):
        continue
    # append our new font to the string
    myString.append(
        myFont+' ', # append the font name as a string
        font=myFont, # set the font
        fill=(random(), random(), random()) # set the fill color
    )
    # max out after 500
    if myNumber > 500:
        break
        
# now draw

# set a margin
myMargin = 50
# draw the bounds of the text box
# rect(myMargin, myMargin, width()-myMargin*2, height()-myMargin*2)

# draw the text box
textBox(
    myString, 
    (
        myMargin, 
        myMargin, 
        width()-myMargin*2, 
        height()-myMargin*2
    )
)