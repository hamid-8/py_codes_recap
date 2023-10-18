#Exercise 3: Use urllib to replicate the previous exercise
# of (1) retrieving the document from a URL, (2) displaying
# up to 3000 characters, and (3) counting the overall number#
# of characters in the document. Don't worry about the
# headers for this exercise, simply show the first 3000
# characters of the document contents.

import urllib.request, urllib.parse, urllib.error

url = input('Enter the URL: ')
tmp = url.split('/')
#print(tmp)
try:
    fhand = urllib.request.urlopen(url)
except:
    print('URL in bad format')
    quit()
counts = 0
for stuff in fhand:
    line = stuff.decode().strip()
    words = line.split()
    counts = counts + len(line)
    if counts <=3000:
        print(line)
print('*****Total number of characters:', counts)
