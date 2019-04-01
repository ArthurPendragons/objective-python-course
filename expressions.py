<<<<<<< HEAD
import re
#Regex = Regular Expression
# text = 'Hey, call me, my number is 01524 844257 & 07976 120498'
# phonenumfinder = re.compile(r'(\d\d\d\d\d) \d\d\d\d\d\d')
# mo = phonenumfinder.search(text)

# text = 'Batman vs superman in the Batmobile mega chase'
# batRegex = re.compile(r'bat(man|mobile|boomerang|copter)')
# mo = batRegex.findall(text.lower())

# print(mo)


# batRegex = re.compile(r'Bat(wo)?man')
# mo = batRegex.search('The adventures of Batwoman')

# print(mo.group())

# phoneRegex = re.compile(r'(\d\d\d\d\d)? \d\d\d\d\d\d')
# mo = phoneRegex.search('My phone number is 01524 844257')
# print(mo.group())
# * is 0 or More = re.compile(r'bat(wo)*man') = wowowowowowowoman wil work
# + is 1 Or more.

# batmanRegex = re.compile(r'Bat(wo)+man')
# mo = batmanRegex.search('Batman vs Superman')

# if mo == None:
# 	print('No Match objects found')
# else:
# 	print(mo.group())


# haRegex = re.compile(r'(Ha){3,7}')

# mo = haRegex.search('HaHaHaHaHaHa')

# print(mo.group())
#Greedy numbers - it wil also go for the larger numbers
# digitRegex = re.compile(r'(\d){3,5}?')
# print(digitRegex.search('1234567890'))
=======
# match object = MO

import re
text = 'my number is 01524 844257'
phonenumfinder = re.compile(r'\d\d\d\d\d \d\d\d\d\d\d')
mo = phonenumfinder.search(text)

print(mo)
>>>>>>> 2e9c96fc28eac6ae796d15be48a1a04bce7f3103
