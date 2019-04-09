import re
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# print(phoneNumRegex.findall('Call: 415-555-9999 Work: 212-222-5555'))
# ['415-555-9999', '212-222-5555']
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print(phoneNumRegex.findall('Call: 415-555-9999 Work: 212-222-5555'))
# [('415', '555', '9999'), ('212', '222', '5555')]
