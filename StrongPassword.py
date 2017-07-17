#! python3

import re, pyperclip

print(
"""
Program detects a strong password which :
- is at least 8 characters long
- contains both uppercase and lowercase letters
- contains at least one digit
"""
)
print('Input a a strong password: ')



regexUp = re.compile(r'[A-Z]+')

regexLw = re.compile(r'[a-z]+')

regexDigit = re.compile(r'\d+')


while True:

    password =  input()
    if len(password) < 8:           # 8 - characters check
        print('Password must be above 8 characters')
        continue

    match = regexUp.search(password)
    if match == None:             # Upper-case check
        print('Password must contain at least one upper case letter')
        continue
        
    match2 = regexLw.search(password)
    if match2 == None:             # Lower-case check
        print('Password must contain at least one lower case letter')
        continue

    match3 = regexDigit.search(password)
    if match3 == None:             # At least one digit check
        print('Password must contain at least one digit')
        continue
    pyperclip.copy(password)
    print('Well done, your strong password has been copied to the clipboard')
    break
    
