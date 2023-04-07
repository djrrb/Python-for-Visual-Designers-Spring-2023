##################
##################
##################

# if you copy this chunk into the top of your script
# you can use the fillHex('#000000') and strokeHex('#000000') functions
# to assign the current fill or stroke

def hex2rgb(myHexString):
    # this is a function that converts a hex string '#FF0000' to a list of RGB values
    # remove any pound sign that precedes the string so we are just looking at the
    # numbers 0–9 and letters A–F
    myHexString = myHexString.lstrip('#')
    # determine how many characters are in the hex string
    # by making this a variable we can deal with both RGB and RGBA values
    myHexLength = len(myHexString)
    # create an empty list to catch the color values that we process
    myColors = []
    # now we will loop through a range of numbers between 0 and the length of our hex string
    # but will skip every other number so that we process the characters in pairs
    for myIndex in range(0, myHexLength, 2):
        # use in index to slice the string
        myHexColorPair = myHexString[myIndex : myIndex + 2]
        # by converting to an integer with base 16
        # we get the value between 0 and 255
        my255ColorValue = int(myHexColorPair, 16)
        # drawbot wants the value between 0 and 1, so we divide by 255
        myColorValue = my255ColorValue / 255
        # now we add the color value to our list
        myColors.append(myColorValue)
    # when we are done, return all color values we have found as a tuple
    return tuple(myColors)

def fillHex(myHexValue):
    # this function uses hex2rgb to convert the value, and then applies the fill
    fill(*hex2rgb(myHexValue))
    
def strokeHex(myHexValue):
    # this function uses hex2rgb to convert the value, and then applies the stroke
    stroke(*hex2rgb(myHexValue))

####################
####################
####################

myForegroundHex = '#006699AA' # a semitransparent blue
myBackgroundHex = '#FF0000' # red

# draw the shape in the back first
# fill with red
fillHex(myBackgroundHex)
# draw a rectangle that is half the width of the canvas and the full height
rect(0, 0, width()/2, height())
# now fill with semitransparent blue
fillHex(myForegroundHex)
# now draw a circle
oval(200, 200, 600, 600)

saveImage('convertHexColors.png')