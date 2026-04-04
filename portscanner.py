import sys
import socket

def is_open(target, port):
    print("is_open" + str(target) + str(port))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    s.close()
    if result == 0:
        return True
    return False


if len(sys.argv) != 2:
    print("Invalid number of arguments")
    sys.exit(-1)

target_hostname = sys.argv[1]
target_ip = socket.gethostbyname(target_hostname)
print("Target Hostname  " + target_hostname)
print("Target IP        " + target_ip)

total_open = 0
for port in range(1,6):
    if is_open(target_ip, port):
        print(f"Port {port} is open")
        total_open += 1

print(f"Total open ports: {total_open}")
