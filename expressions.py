# match object = MO

import re
text = 'my number is 01524 844257'
phonenumfinder = re.compile(r'\d\d\d\d\d \d\d\d\d\d\d')
mo = phonenumfinder.search(text)

print(mo)