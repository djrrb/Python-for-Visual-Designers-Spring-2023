# import the os module
# allows us to list directories


# this will run on any image in the /images directory

import os

# what is my directory name
myDirectory = 'images'

# what extensions do i want to process
myExtensions = ['.jpg', '.png', '.gif']

# get a list of filenames in our directory using os.listdir()
myFilenames = os.listdir(myDirectory)

# loop through each file
for myFilename in myFilenames:
    myExtension = os.path.splitext(myFilename)[1]
    # test to make sure the extension 
    if myExtension in myExtensions:
    #if myFilename.endswith('.jpg'):
    

        # if i like the file, draw it to canvas
        newPage()
        # i have to get the full path, including the folder
        # so join the folder and filename
        myPath = os.path.join(myDirectory, myFilename)
        # make an image 
        myImage = ImageObject(myPath)
        # do a filter
        myImage.twirlDistortion()
        # draw the image
        image(myImage, (0, 0))
    