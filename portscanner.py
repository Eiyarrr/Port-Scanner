import sys
import socket
import asyncio

async def is_open(target, port):
    _, writer = await asyncio.wait_for(asyncio.open_connection(target, port), timeout = 1)
    print(f"Port {port} is open")
    writer.close()
    await writer.wait_closed()
    return True

async def main():
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        sys.exit(-1)

    hostname = sys.argv[1]
    target = socket.gethostbyname(hostname)
    print("Target Hostname  " + hostname)
    print("Target IP        " + target)

    all_ports = [is_open(target, port) for port in range(1, 65535)]
    results = await asyncio.gather(*all_ports)
    
    total_open = sum(results)

    print(f"Total open ports: {total_open}")

asyncio.run(main())
