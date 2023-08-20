lst = list()
while True:
    x = input('Enter a number OR done: ')
    if x == 'done':
        break
    try:
        num = float(x)
    except:
        print('Not a number')
        continue
    lst.append(num)
if lst == []:
    print('Nothing entered!')
else:
    ma = max(lst)
    mi = min(lst)
    print('Maximum:',ma)
    print('Minimum:',mi)
