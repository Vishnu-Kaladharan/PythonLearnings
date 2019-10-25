import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect(('data.pr4e.org',80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()

mysock.send(cmd)
html_result = ''
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
    html_result = html_result + data.decode()

print(f'Please find below the recieved data\n {html_result}')
mysock.close()