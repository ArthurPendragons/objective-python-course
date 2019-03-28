# def isPhoneNumber(message):
# 	if len(message) != 12:
# 		return False
# 	if message[0] != '0':
# 		return False
# 	for i in range(0,3):
# 		if not message[i].isdecimal():
# 			return False
# 	if message[5] != ' ':
# 		return False
# 	for i in range(6-12):
# 		if not message[i].isdecimal():
# 			return False
# 	return True

text_message = 'Call me on my number 07976 120498 or 01524844257 31231238123'

# # foundNumber = False
# # for i in range(len(text_message)):
# # 	chunk = text_message[i:i+12]
# # 	if isPhoneNumber(chunk):
# # 		print('Found phone number: ' + chunk)
# # 		foundNumber = True
# # if not foundNumber:
# # 	print('No number found')



# foundNumber = False

# for i in range(len(text_message)):
# 	chunk = text_message[i:i+12]
# 	if isPhoneNumber(chunk):
# 		print('Number Found: {}'.format(chunk))
# 		foundNumber = True
# if not foundNumber:
# 	print('No number found')

# import re 

# phoneNumRegex = re.compile(r'\d\d\d\d\d \d\d\d\d\d')
# mo = phoneNumRegex.findall(text_message)
# print(mo)

# import re

# phoneNumRegex = re.compile(r'\d\d\d\d\d \d\d\d\d\d')
# phoneNumRegexnospace = re.compile(r'\d\d\d\d\d\d\d\d\d\d\d')

# mo = phoneNumRegex.findall(text_message)
# mo2 = phoneNumRegexnospace.findall(text_message)

# print(' & '.join(mo))

# if phoneNumRegexnospace.search(text_message) == None:
# 	print('No Numbers Found')
# else:
# 	print(phoneNumRegexnospace.findall(text_message))



# def calc(num,num2):
# 	assert(num > 10)
# 	print(num + num2)

# calc(15,10)



import re
text ='01524 844257'

findphone = re.compile(r'0\d\d\d\d \d\d\d\d\d\d')

mo = findphone.search(text)

if mo == None:
	print('No numbers found')
else:
	print(mo.group())
