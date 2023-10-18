#Exercise 2: Change your socket program so that it counts the
# number of characters it has received and stops displaying
# any text after it has shown 3000 characters. The program
# should retrieve the entire document and count the total
# number of characters and display the count of the number#
# of characters at the end of the document.
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input('Enter the URL: ')
tmp = url.split('/')
#print(tmp)
try:
    mysock.connect((tmp[2], 80))
except:
    print('URL in bad format')
    quit()
cmd = 'GET '+url+' HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)
counts = 0
while True:
    data = mysock.recv(3000)
    counts = counts + len(data)
    if len(data) < 1:
        break
    print(data.decode(),end='')
print('*****Total number of characters:', counts)
mysock.close()
