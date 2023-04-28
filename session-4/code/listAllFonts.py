myString = FormattedString(fontSize=25, lineHeight=40)

for myNumber, myFont in enumerate(installedFonts()):
    if myFont.startswith('.'):
        continue
    myString.append(myFont+' ', font=myFont, fill=(random(), random(), random()))
    if myNumber > 500:
        break
        
myMargin = 50
#rect(myMargin, myMargin, width()-myMargin*2, height()-myMargin*2)
textBox(myString, (myMargin, myMargin, width()-myMargin*2, height()-myMargin*2))

print(myString)