myList = ['apples', 'oranges', 'bananas']
print(myList)

for myItem in myList:
    print('go to the store and get', myItem)
    
print(myList[0]) # first item
print(myList[-1]) # last item
print(myList[:2]) # first two items

myList.append('grapefruit')

print(myList)

myList.sort()
print(myList)

myList.reverse()
print(myList)

print('apples' in myList)
print('kiwi' in myList)
print(len(myList))