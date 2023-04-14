# saved state example
with savedState():
    translate(500, 500) # move to center
    fill(1, 0, 0) # set fill to red
    fontSize(100) # make the font size big
    oval(0, 0, 200, 200)
    
    with savedState():
        # go down an alternate timeline
        # set fill to green and shrink everything
        fill(0, 1, 0)
        scale(.5)
        # make a new save state that is rotated
        with savedState():
            rotate(-20)
            rect(200, 200, 200, 200)
        # dedenting returns to 0° rotation
        font('Georgia')
        fill(0)
        text('more text', (0, 0))

# outside of all saved states
# we are back to blue in the lower left corner
fill(0,0,1)
text('hello world', (0, 0))