#!/usr/bin/env/python 3

import random

SECURITY = {}

SECURITY['a'] = '4'
SECURITY['e'] = '3'
SECURITY['i'] = '1'
SECURITY['o'] = '0'
SECURITY['u'] = '&'

SECURITY['l'] = '1'
SECURITY['g'] = 'G'
SECURITY['s'] = '5'
SECURITY['b'] = '8'

temp_pass, password = input().lower().replace(" ",""), ""

first_last = temp_pass[0].title() + temp_pass[-1].title()

for letter in temp_pass:
    if letter not in SECURITY:
        password += letter
    elif letter in SECURITY:
        password += SECURITY[letter]

print(f'{first_last}#{password[::-1]}')
