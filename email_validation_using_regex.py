# a-z small cases , first condition will be alphabet
# digits 0 to 9
# . _ time 1
# @ time 1
# . will be at 3 or 4 position from last

import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
useer_email=input('Enter your email address: ')

if re.search(email_condition, useer_email):
    print('valid email address: ')
else:
    print('Invalid email address: ')