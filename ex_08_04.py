fname = input('Enter file: ')
romeo = open(fname)
output = []
for line in romeo:
#    line = line.rstrip()
    wrds = line.split()
    i = 0
#    print(wrds)
    while i < len(wrds):
        if wrds[i] not in output:
            output.append(wrds[i])
        i = i + 1
output.sort()
print(output)
