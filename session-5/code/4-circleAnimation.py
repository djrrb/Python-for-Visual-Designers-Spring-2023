from easing_functions import *
#print(dir())

myFrames = 24

myXAdvance = width()/myFrames
print(myXAdvance)
myEase1 = SineEaseInOut(0, width(), myFrames)
myEase2 = SineEaseInOut(width(), 0, myFrames)

for myEase in [myEase1, myEase2]:

    for myFrame in range(myFrames):
        newPage()
        frameDuration(1/24)
        fill(1)
        myX = myEase.ease(myFrame)
        print(myFrame, myX)
        rect(0, 0, width(), height())
        fill(0)
        oval(myX-50, 100-50, 100, 100)
    
        # save one image per frame
        #saveImage('myFrame'+str(myFrame)+'.png') 
# save one image for the whole thing
saveImage('circleAnimation.gif')