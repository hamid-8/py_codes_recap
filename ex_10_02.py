fname = input('Enter a file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
handle = open(fname)
counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        ind = words[5].find(':')
        hour = words[5][:ind]
        if hour not in counts:
            counts[hour] = 1
        else :
            counts[hour] = counts[hour] + 1
#print(counts)
tups = counts.items()
#print(tups)
tmp =list()
for k, v in tups:
    tmp.append((k, v))
tmp = sorted(tmp)
i = 0
b = len(tmp)
while i < b:
    print(tmp[i][0], tmp[i][1])
    i = i + 1
