import re

split_term= '@'
email = 'me@me.com'
print(re.split(split_term, email))

patterns = ['term1', 'term2']
text=  'This is a string with term1'
for pattern in patterns:
    print('search for :'+pattern)
    match = re.search(pattern, text)
    
