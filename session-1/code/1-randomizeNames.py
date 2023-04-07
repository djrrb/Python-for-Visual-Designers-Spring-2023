# import the shuffle function from the random library
from random import shuffle

# define a variable called ourNames as a multiline string
# split that 
ourNames= """Banu
Simona
Aitana
Ying
May
Xiaoyi
Cynthia
Setareh
Sarah
Ji Woo
Sau
Louis
Renee
Richard"""

# convert that string into a list by splitting it at each new line
ourNamesList = ourNames.split('\n')

# print the original list
print(ourNamesList)

# shuffle the list 
shuffle(ourNamesList)

# print it again
print(ourNamesList)

# give me a clean printout
# by looping through each name and printing them one at a time
for oneName in ourNames:
    print(oneName)
