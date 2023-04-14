# set the font size
fontSize(100)

# move to the center of the canvas
translate(500, 500)
# draw a rectangle at (0, 0)
# which is now the center of the canvas
rect(0, 0, 100, 100)
# move 250 to the right and 250 down
translate(250, -250)
# draw text at (0, 0), which is now in 
# the lower right of the canvas
text('hello world', (0, 0))

