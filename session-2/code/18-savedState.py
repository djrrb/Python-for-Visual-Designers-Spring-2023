# my default color is red
# i want most things in my document to be red

fill(1, 0, 0)
oval(0, 900, 100, 100)

# but i want the one rectangle to be black
# so i put that in the saved state
with savedState():
    fill(0)
    rect(0, 0, 100, 100)

# the second i exit the saved state
# by dedenting, i am back to red
oval(500, 500, 100, 100)

fontSize(100)
text('hello world', (500, 0))
