import pyfiglet 
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PROTO PORT SCANNER")
print(ascii_banner)

target = input(str("Target IP: "))

#Banner
print("_" * 50)
print("Scanning Target: " + target) 
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)

try:

    #Scan most common ports on the target ip
    for port in range(1,1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        #Return open port
        result = s.connect_ex((target,port))
        if result == 0:
            print("[*] Port {} is open".format(port))
            s.close()
            
            
except KeyboardInterrupt: 
    print("\n Exiting :(")
    sys.exit()

except socket.error: 
    print("\ Host not responding :(")
    sys.exit()
    