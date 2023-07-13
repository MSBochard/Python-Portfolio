'''
Algorithm:  Script to show the Request and Response cycle headers through
            opening a socket.
'''
#Importes the socket library
import socket

#Opens the socket, connects to the data.pr4e.org webpage
#through TCP port 80 and sends GET request
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mySock.send(cmd)

#Grabs first 512 characters of recieved information, verifies that the
#information was recieved, and prints the data
while True:
    data = mySock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

#Closes the socket
mySock.close()
