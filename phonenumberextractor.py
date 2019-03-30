#! python3



#TODO: Copy the extracted email/phone to clipboard
import re, pyperclip, itertools


#TODO: Create a regex for phone numbers 
phoneRegex = re.compile(r'''
(											# 415-555-0000, 555-0000, 415 555-0000 ext 12345, ext. 12345, x12345
			((\d\d\d) | (\(\d\d\d\)))?
			(\s|-)
			\d\d\d
			-
			\d\d\d\d
)
			''', re.VERBOSE)


#TODO: Create a regex for email addresses

emailRegex = re.compile(r'''
			[a-zA-Z]+
			@
			[a-zA-Z0-9]+
			\.
			[a-zA-Z0-9]{0,3}


						''', re.VERBOSE)
			# something@something.com




#TODO: Get the text off the clipboard

text = pyperclip.paste()

#TODO: extract te email / phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
	allPhoneNumbers.append(phoneNumber[0])

# for email in extractedEmail:
# 	for phone in extractedPhone:
# 		print('My email is {} and my number is {}'.format(email,phone[0]))
	
# sentence = (['my email is: {} and my number is {}'.format(*i) for i in zip(extractedEmail,allPhoneNumbers)])

# for letter in sentence:
# 	print(letter)

results = '\n'.join(extractedEmail) + '\n' + '\n'.join(allPhoneNumbers)
print(results)
