
myString = 'HELLO WORLD'

# string methods
print(myString.upper())
print(myString.lower())
print(myString.replace('HELLO', 'GOODBYE'))
print(myString.split(' '))
print('&'.join(['John', 'Paul', 'George', 'Ringo']))

# formatted string
myName = 'David'
print('Hello my name is ' + myName + ' and that is all.')
print(f'Hello my name is {myName} and that is all.')

# slicing
print(myString[0]) # give me first item
print(myString[0:5]) # give me first five items
print(myString[-1]) # give me last item
print(myString[-5:]) # give me last five items

# other stuff
print(len(myString))
print('HELLO' in myString)
print('GOODBYE' in myString)