myList = ['apples', 'oranges', 'bananas']
print(myList)

# loop through a list
for myItem in myList:
    print('go to the store and get', myItem)
    
# slice a list
print(myList[0]) # first item
print(myList[-1]) # last item
print(myList[:2]) # first two items

# append to a list
myList.append('grapefruit')
print(myList)

# sort a list
myList.sort()
print(myList)

# reverse a list
myList.reverse()
print(myList)

# test a list
print('apples' in myList)
print('kiwi' in myList)

# determine the length
print(len(myList))