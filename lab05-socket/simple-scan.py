import socket
import errno
import os
from datetime import datetime

#SERVER_PORT = 80
SERVER_PORT = 54321

#SERVER_HOST = 'scanme.nmap.org'
#SERVER_HOST = 'sharnet.sharlab.my'
SERVER_HOST = 'xxx.yy'

print('Scanning port(s) at: ',SERVER_HOST)
stime = datetime.now()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(20)

try:
    result = sock.connect_ex((SERVER_HOST, SERVER_PORT))
    if result == 0:
        print(SERVER_PORT, '--> Open')
    elif result in (errno.EAGAIN, errno.ETIMEDOUT):
        print(SERVER_PORT, '--> No answer (timed out, maybe a firewall)')
    else:
        name = errno.errorcode.get(result, 'UNKNOWN')
        print(SERVER_PORT, '--> Closed : Reason:', name, '-',os.strerror(result))

except OSError as e:
    print('Error:', e)
finally:
    sock.close()

print('Port Scanning Completed in: ',datetime.now() - stime)
