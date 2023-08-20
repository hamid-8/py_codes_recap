fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('The file',fname,'not found!')
    quit()
for line in fhand:
    line2 = line.rstrip()
    print(line2.upper())
