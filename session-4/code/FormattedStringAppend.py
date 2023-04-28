myString = FormattedString(
    'Hello', 
    fontSize=100, 
    fill=(0, 0, 1),
    tracking=10,
    font='MinionPro-Regular',
    openTypeFeatures={'smcp': True},
)

myString.append(' world', fill=(1, 0, 0), font='MinionPro-It', tracking=-10)

text(myString, (0, 0))

