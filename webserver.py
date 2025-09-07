from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 8080
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() 
    try:
        message = connectionSocket.recv(1024).decode() 
        filename = message.split()[1]
        f = open(filename[1:], 'r')

        outputdata = f.read()
        f.close()

        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
        connectionSocket.send(header.encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        body = "<html><body><h1>404 Not Found</h1></body></html>"
        header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
        connectionSocket.send(header.encode())
        connectionSocket.send(body.encode())

        connectionSocket.close()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
