from easing_functions import *
#print(dir())

font('CondorVariable-VF.ttf', 200)
myAxis = 'wght'
myMinValue = listFontVariations()[myAxis]['minValue']
myMaxValue = listFontVariations()[myAxis]['maxValue']
print(myMinValue, myMaxValue)

myFrames = 24

myXAdvance = width()/myFrames
print(myXAdvance)
myEase1 = SineEaseInOut(myMinValue, myMaxValue, myFrames)
myEase2 = SineEaseInOut(myMaxValue, myMinValue, myFrames)

for myEase in [myEase1, myEase2]:

    for myFrame in range(myFrames):
        newPage()
        font('CondorVariable-VF.ttf', 200)
        frameDuration(1/24)
        fill(1)
        myValue = myEase.ease(myFrame)
        rect(0, 0, width(), height())
        fill(0)
        oval(myValue-50, 100-50, 100, 100)
        fontVariations(**{myAxis: myValue})
        #fontVariations(wght=myValue)
        text('Variable!', (width()/2, height()/2), align="center")
    
        # save one image per frame
        #saveImage('myFrame'+str(myFrame)+'.png') 
# save one image for the whole thing
saveImage('variableFontAnimation.gif')