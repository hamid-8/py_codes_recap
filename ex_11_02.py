import re
fname = input('Enter a file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
handle = open(fname)
count = 0
sum = 0
for line in handle:
    stuff = re.findall('^New Revision: ([0-9.]+)',line)
    if len(stuff) != 1 : continue
    #print(stuff)
    num = float(stuff[0])
    sum = sum + num
    count = count + 1
print(sum/count)
