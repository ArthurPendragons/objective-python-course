import re


text = "megasknight@msn.com jake.p.burgess@gmail.com"

emailaddressRegex = re.compile(r'(.*?.com)')

print(emailaddressRegex.findall(text))
