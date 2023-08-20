ccc = dict()
while True:
    x = input('Enter the name: ')
    if x == 'done' :
        break
    if x not in ccc :
        ccc[x] = 1
    else :
        ccc[x] = ccc[x] + 1
print(ccc)
# Check this:
# counts = ccc.get(name, 0)
