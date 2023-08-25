import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('^From (\S+@\S+)',x)
y = re.findall('[0-9]+',x)
y = re.findall('[AEIOU]+',x)
y = re.findall('\S+@\S+',x)
print(y)
# test
