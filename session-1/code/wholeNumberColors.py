# each of these is a list with two options [0, 1]
myRedOptions = range(2)
myGreenOptions = range(2)
myBlueOptions = range(2)

# loop through all three to get all permutations
for myRedOption in myRedOptions:
    for myGreenOption in myGreenOptions:
        for myBlueOption in myBlueOptions:
            # make a new page
            newPage()
            # draw our color as the background
            fill(myRedOption, myGreenOption, myBlueOption)
            rect(0, 0, width(), height())
            
            # draw a black background so we can always see the text
            fill(0)
            rect(0, 0, 400, 200)
            # make the text white and 50pt
            fill(1)
            fontSize(50)
            # convert our numbers to strings so we can draw them as text
            myColorLabel = str(myRedOption) + ' ' + str(myGreenOption) + ' ' + str(myBlueOption)
            # draw our string as text
            text(myColorLabel, (200, 80), align="center")
            
            
saveImage('wholeNumberColors.pdf')