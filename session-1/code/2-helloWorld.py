# print a string to the console
print('hello world')

# set the font size
fontSize(125)
# set the font
font('ComicSansMS-Bold')

# print the number of installed fonts
print(len(installedFonts()), 'installed fonts')

# print all installed fonts as a list
print(installedFonts())




# set the fill
fill(203/255, 113/255, 167/255) # red green blue

# draw some text to the canvas
# text('text to write', (x, y))
text('hello world', (170, 460))

# save the image in a couple formats
saveImage('helloWorld.png')
saveImage('helloWorld.gif')
saveImage('helloWorld.pdf')