import sys
import socket
import asyncio
import argparse


async def is_open(target, port, semaphore):
    async with semaphore:
        try:
            _, writer = await asyncio.wait_for(
                asyncio.open_connection(target, port), timeout=1
            )
            print(f"Port {port} is open")
            writer.close()
            await writer.wait_closed()
            return True
        except asyncio.TimeoutError:
            return False
        except OSError:
            print(f"OSError {OSError} at port {port}")
            return False


def parse_user_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "hostname",
        help="Hostname / IP Address of target to scan the ports of",
        type=str,
    )
    parser.add_argument(
        "semaphore",
        nargs="?",
        help="Size of the semaphore to use when scanning (default = 1000)",
        type=int,
        default=1000,
    )
    args = parser.parse_args()

    try:
        target = socket.gethostbyname(args.hostname)
    except socket.gaierror:
        print("Failed to parse hostname!")
        sys.exit(-1)

    semaphore = asyncio.Semaphore(args.semaphore)

    return args.hostname, target, semaphore


async def main():
    hostname, target, semaphore = parse_user_args()

    print("Target Hostname  " + hostname)
    print("Target IP        " + target)
    print("Semaphore Size   " + str(semaphore._value) + "\n")

    all_ports = [is_open(target, port, semaphore) for port in range(1, 65535)]
    results = await asyncio.gather(*all_ports)

    total_open = sum(results)

    print(f"Total open ports: {total_open}")


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("\nKeyboardInterrupt occurred! Exiting program!")
    sys.exit(1)
