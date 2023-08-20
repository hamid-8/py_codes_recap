fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if not line.startswith('From ') :
        continue
    wrds = line.split()
    print(wrds[1])
    count = count + 1
print('There were', count, 'lines in the file with From as the first word')
