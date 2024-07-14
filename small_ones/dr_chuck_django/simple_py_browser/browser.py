import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('localhost',9000))
cmd = 'GET http://localhost:9000 HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end = '')

mysock.close()