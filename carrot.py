import re


text = 'He said hello world!'
beginsWithHelloRegex = re.compile(r'^Hello')
endsWithHelloRegex = re.compile(r'world!$')
print(beginsWithHelloRegex.search(text))
print(endsWithHelloRegex.search(text))

allDigitsRegex = re.compile(r'^\d+\w?\d+$')
# print(allDigitsRegex.search('5551239812388313'))

atRegex = re.compile(r'.{1,2}at')

atRegex = re.compile(r'.*')


print(atRegex.findall('The cat in the hat sat on the flat mat'))

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Jake Last Name: Burgess'))

text='''
Hey James,

Username: Brownjl
Password: Qwerty123

Thanks,

Jake
'''


passwordRegex = re.compile(r'password:(.*)', re.I)
print(passwordRegex.findall(text))


# prime ='Serve the public trust. \nProtect the innocent. \nUphold the law'

# dotStar =re.compile('.*', re.DOTALL)
# print(dotStar.search(prime))

# vowelRegex = re.compile(r'[aeiou]', re.I)
# print(vowelRegex.findall('Al, Why does your programming book talk about robocop'))


namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret document to Agent Mueller'))

print(namesRegex.sub(r'Agent \1','Agent Alice gave the secret document to Agent Mueller'))

text = ' Number is 01524 844257'

phonenumRegex = re.compile(r''' 
							(\d\d\d\d\d\s) |
							(\d\d\d\d\d) #OR without a space
							(\d\d\d\d\d\d)''', re.VERBOSE)

print(phonenumRegex.search(text))
