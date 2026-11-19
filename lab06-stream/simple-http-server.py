import socket, sys

#SERVER_HOST = '192.168.219.128'
SERVER_HOST = 'sharnet.sharlab.my'
SERVER_PORT = 54322

try:
    serv_sock = socket.create_server((SERVER_HOST, SERVER_PORT), family=socket.AF_INET, backlog=20)

except (OSError, ValueError) as e:
    print('Cannot start server:',e)
    sys.exit(1)

#for testing
#print('SO_REUSEADDR =', serv_sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR))

print('Simple HTTP Server:', serv_sock.getsockname())
try:
    while True:
        print('\n\nServer waiting for a connection request ...')
        cli_sock, cli_addr = serv_sock.accept()
        print('HTTP request received from:',cli_addr)
        try:
            cli_sock.settimeout(10)
            request = cli_sock.recv(1024).decode(errors='replace')
            print(request)

            welcome = 'Welcome client: ' + cli_addr[0]
            print(welcome)
            body = 'Network Programming Course\n' +welcome+'\n'
            body_bytes=body.encode('utf-8')

            response=('HTTP/1.1 200 OK\r\n' +
                      'Content-Type: text/plain; charset=utf-8\r\n' +
                      'Content-Length: ' + str(len(body_bytes)) + '\r\n' +
                      'Connection: close\r\n' +
                      '\r\n')
            cli_sock.sendall(response.encode('utf-8')+body_bytes)
        except OSError as e:
            print('Problem with client', cli_addr,':',e)
        finally:
            cli_sock.close()
except KeyboardInterrupt:
    print('You pressed <CTRL> C to exit')
finally:
    serv_sock.close()

