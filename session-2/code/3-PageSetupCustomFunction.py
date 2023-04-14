# make a function to group a bunch of code
# that we want to run multiple times
# this saves us the trouble of running
# each function on each page
def myPageSetup():
    fill(1, 0, 0)
    font('Verdana')
    fontSize(100)


# make a new page
newPage('Letter')
myPageSetup()
text('hello world', (100, 100))

# make another new page
newPage('LetterLandscape')
myPageSetup()
text('this is page 2', (100, 100))