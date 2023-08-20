fname = input('Enter a file name: ')
handle = open(fname)
counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        email = words[1]
        ind = email.index('@')
        domain = email[ind+1:]
        if domain not in counts:
            counts[domain] = 1
        else :
            counts[domain] = counts[domain] + 1
print(counts)
