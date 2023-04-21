import os

myDirectory = 'images'

myExtensions = ['.jpg', '.png', '.gif']

myFilenames = os.listdir(myDirectory)
for myFilename in myFilenames:
    if os.path.splitext(myFilename)[1] in myExtensions:
    #if myFilename.endswith('.jpg'):
        newPage()
        myPath = os.path.join(myDirectory, myFilename)
        print(myFilename)
        print(myPath)
        
        myImage = ImageObject(myPath)
        myImage.twirlDistortion()
        image(myImage, (0, 0))
    