str = 'X-DSPAM-Confidence: 0.8475 '
print(str)
p = str.find(':')
print(p)
piece = str[p+1:].strip()
print(piece)
value = float(piece)
print(value)
