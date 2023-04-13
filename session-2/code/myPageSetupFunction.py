

def myPageSetup():
    fill(1, 0, 0)
    font('Verdana')
    fontSize(100)

    
newPage('Letter')
myPageSetup()
text('hello world', (100, 100))

newPage('LetterLandscape')
myPageSetup()
text('this is page 2', (100, 100))