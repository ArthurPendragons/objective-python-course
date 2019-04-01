import re

lyrics = '''
On the twelfth day of Christmas
my true love sent to me:
12 Drummers Drumming
11 Pipers Piping
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and 1 Partridge in a Pear Tree1

'''


# xmasRegex = re.compile(r'\d+\s\w+')
# print(xmasRegex.findall(lyrics))


# doublevowelregex = re.compile(r'[aeiouAEIOU]{2}') # Will find 2 in the sequence in a ro


# import re


# findwordRegex = re.compile(r'(\w+)')

# print(findwordRegex.findall('We are one fort heavy metal suicide)cat'))


lyricRegex = re.compile(r'\d\d?\s\w+')
numbers = lyricRegex.findall(lyrics)
print('\n'.join(numbers))