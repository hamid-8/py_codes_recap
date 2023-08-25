import re
fname = input('Enter a file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
handle = open(fname)
reg = input('Enter regular expression: ') # regular expression
count = 0
for line in handle:
    match = re.findall(reg,line)
    if len(match) > 0:
        count = count + 1
print(fname,'had',count,'lines that matched',reg)
