fname = input('Enter a file name: ')
handle = open(fname)
counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        if words[2] not in counts:
            counts[words[2]] = 1
        else :
            counts[words[2]] = counts[words[2]] + 1
print(counts)
