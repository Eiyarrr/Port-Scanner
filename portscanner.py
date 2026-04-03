import sys

if len(sys.argv) != 2:
    print("Invalid number of arguments")
    sys.exit(-1)

target = sys.argv[1]
print("Target: " + target)

for port in range(1,65535):
    if is_open(port):
        print("Port {} is open")

def is_open(port):
    return true
    #check if open
