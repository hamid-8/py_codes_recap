fname = input('Enter a file name: ')
handle = open(fname)
counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        if words[1] not in counts:
            counts[words[1]] = 1
        else :
            counts[words[1]] = counts[words[1]] + 1
#print(counts)
#print('***************')
tups = counts.items()
#print(tups)
#print('*********************')
tmp =list()
for k, v in tups:
    tmp.append((v, k))
tmp = sorted(tmp, reverse=True)
print(tmp[0][1], tmp[0][0])
