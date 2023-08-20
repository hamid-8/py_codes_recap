fname = input('Enter a file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
hand = open(fname)
alfabet = dict()
tmp = 'abcdefghijklmnopqrstuvwxyz'
for i in tmp:
    alfabet[i] = 0
#print(alfabet)

for line in hand:
    words = line.split()
    for word in words:
        word = word.lower()
        for letter in word:
            if letter in alfabet:
                alfabet[letter] = alfabet[letter] + 1
tups = alfabet.items()
#print(tups)
freq =list()
for k, v in tups:
    freq.append((v, k))
freq = sorted(freq, reverse=True)
print(freq)
i = 0
b = len(freq)
while i < b:
    print(freq[i][1], freq[i][0])
    i = i + 1
