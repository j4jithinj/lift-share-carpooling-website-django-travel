import re
r = '^[A-Z]{2}[ -][0-9]{1,2}(?: [A-Z])?(?: [A-Z]*)? [0-9]{4}$'
s = '325353'
print(re.search(r,s))