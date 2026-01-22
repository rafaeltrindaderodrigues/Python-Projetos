import re

pattern = r'\d\d\d\d\d\d\d\d\d\d'
text = 'My phone number is 123425623178910'
match = re.search(pattern, text)

if match:
    print('Phone number found: ', match.group())
else:
    print('No match')

s2 = "The bodyguards is the best album of Whitney Houston"
result = re.findall('is', s2)
print(result)

pat = r'Whitney Houston'
replacement = 'legend'

new_string = re.sub(pat, replacement, s2, flags=re.IGNORECASE)
print(new_string)


