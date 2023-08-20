fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('The file',fname,'not found!')
    quit()
count = 0
f = -1
total = 0
for line in fhand:
    f = line.find('X-DSPAM-Confidence')
    if f != -1:
        count = count + 1
        value = float(line[f+19:].strip())
        total = total + value
    f = -1
print('Average spam Confidence:',total/count)
