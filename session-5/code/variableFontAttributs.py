font('CondorVariable-VF.ttf', 200)

print(listFontVariations())

myAxis = 'wght'
myMinValue = listFontVariations()[myAxis]['minValue']
myMaxValue = listFontVariations()[myAxis]['maxValue']

fontVariations(wght=340, wdth=70)
text('This is text', (0, 0))


#myDict = {'peanut butter': 'jelly'}
#print(myDict['peanut butter'])