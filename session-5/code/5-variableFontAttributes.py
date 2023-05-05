# set the font
font('CondorVariable-VF.ttf', 200)
# list the font variations
print(listFontVariations())

# lookup an axis by tag
myAxis = 'wght'
# get its min and max values
myMinValue = listFontVariations()[myAxis]['minValue']
myMaxValue = listFontVariations()[myAxis]['maxValue']
print(myMinValue, myMaxValue)

# set values explicitly
fontVariations(wght=340, wdth=70)

# alternatively, you can write it as an unpacked dictionary
#fontVariations(**{'wght': 340, 'wdth': 70})

# draw the text
text('This is text', (0, 0))