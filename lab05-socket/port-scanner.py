import socket
import errno
import os
from datetime import datetime

# Interactive user inputs
SERVER_HOST = input("Enter target IP address or domain name: ").strip()

while True:
    try:
        start_port = int(input("Enter start port (e.g., 20): ").strip())
        end_port = int(input("Enter end port (e.g., 100): ").strip())
        if 1 <= start_port <= 65535 and 1 <= end_port <= 65535 and start_port <= end_port:
            break
        print("Invalid range. Ensure ports are between 1 and 65535, and start <= end.")
    except ValueError:
        print("Please enter valid integers for port numbers.")

print(f"\nScanning ports {start_port} to {end_port} on: {SERVER_HOST}")
stime = datetime.now()

for port in range(start_port, end_port + 1):
    # A new socket must be created for each connection attempt
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2.0)  # Reduced from 20s to prevent long hangs across ranges

    try:
        result = sock.connect_ex((SERVER_HOST, port))
        if result == 0:
            print(f"Port {port:5d} --> Open")
        elif result in (errno.EAGAIN, errno.ETIMEDOUT):
            print(f"Port {port:5d} --> No answer (timed out, maybe a firewall)")
        else:
            name = errno.errorcode.get(result, 'UNKNOWN')
            print(f"Port {port:5d} --> Closed : Reason: {name} - {os.strerror(result)}")
    except OSError as e:
        print(f"Port {port:5d} --> Error: {e}")
    finally:
        sock.close()

print(f"\nPort Scanning Completed in: {datetime.now() - stime}")