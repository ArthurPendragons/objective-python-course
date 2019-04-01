import re

text = '01524 844257, 07976 120498'
phoneRegex = re.compile(r'\d\d\d\d\d \d\d\d\d\d\d')

mo = len(phoneRegex.findall(text))
print(mo)