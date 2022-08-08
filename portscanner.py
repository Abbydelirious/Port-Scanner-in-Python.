import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

if len(sys.argv) == 2:

    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of argument, You must Enter the IP address")

print("-" * 50)
print("Scanning The Target::" + target)
print("Scanning Started at::" + str(datetime.now()))
print("-" * 50)

try:

    for port in range(1,100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(2)

        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
        print("\n Exitting Program")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could not be resolved")
        sys.exit()
except socket.error:
        print("\n Server Not Responding")
        sys.exit()
    
    

