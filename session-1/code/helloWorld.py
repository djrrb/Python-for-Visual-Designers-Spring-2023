print("""hello world 




what's up""")
fontSize(125)
font('ComicSansMS-Bold')
fill(203/255, 113/255, 167/255) # red green blue
text('hello world', (170, 460))

print(len(installedFonts()))

saveImage('/Users/david/Desktop/helloWorld.jpg')
saveImage('helloWorld.png')
saveImage('helloWorld1.gif')