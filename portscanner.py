import sys
import socket

def is_open(port):
    #check if open
    return port


if len(sys.argv) is not 2:
    print("Invalid number of arguments")
    sys.exit(-1)

target_hostname = sys.argv[1]
target_ip = socket.gethostbyname(target_hostname)
print("Target Hostname  " + target_hostname)
print("Target IP        " + target_ip)

total_open = 0
for port in range(1,65535):
    if is_open(port):
        print("Port {} is open")
        total_open += 1

print("Total open ports: " + str(total_open))
