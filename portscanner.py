import sys
import socket
import asyncio

async def is_open(target, port, semaphore):
    async with semaphore:
        try:
            _, writer = await asyncio.wait_for(asyncio.open_connection(target, port), timeout = 1)
            print(f"Port {port} is open")
            writer.close()
            await writer.wait_closed()
            return True
        except asyncio.TimeoutError:
            return False
        except OSError:
            print(f"OSError {OSError} at port {port}")
            return False

async def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Invalid number of arguments")
        sys.exit(-1)

    semaphore = asyncio.Semaphore(1000)
    if len(sys.argv) == 3:
        try:
            semaphore = asyncio.Semaphore(int(sys.argv[2]))
        except Exception:
            print(f"Incorrect argument caused {Exception}!")

    hostname = sys.argv[1]
    target = socket.gethostbyname(hostname)
    print("Target Hostname  " + hostname)
    print("Target IP        " + target)
    print("Semaphore Size   " + str(semaphore._value))

    all_ports = [is_open(target, port, semaphore) for port in range(1, 65535)]
    results = await asyncio.gather(*all_ports)
    
    total_open = sum(results)

    print(f"Total open ports: {total_open}")

asyncio.run(main())
