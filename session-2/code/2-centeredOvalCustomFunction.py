# create a custom function
# that takes four arguments
def centeredOval(myX, myY, myWidth, myHeight):
    # all this code is part of the function
    # pass the arguments to the default oval() function
    # but offset the X and Y by half the shape height
    oval(
        myX-myWidth/2, 
        myY-myHeight/2, 
        myWidth, 
        myHeight
    )
    
# now we're in the main script

# draw a couple ovals to see the function in action
centeredOval(width()/2, height()/2, 230, 210)

centeredOval(200, 200, 500, 500)