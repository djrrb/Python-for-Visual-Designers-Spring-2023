with savedState():
    translate(500, 500) # move to center
    fill(1, 0, 0) # set fill to red
    fontSize(100)

    with savedState():
        oval(0, 0, 200, 200)
        fill(0, 1, 0)
        scale(.5)
        with savedState():
            rotate(-20)
            rect(200, 200, 200, 200)
        font('Georgia')
        fill(0)
        text('more text', (0, 0))

fill(0,0,1)
text('hello world', (0, 0))