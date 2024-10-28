#######################################
#                                     #
#  Script created by Mark L. Jensen   #
#  marklustyjensen@gmail.com          #
#  www.marklustyjensen.com            #
#                                     #
#######################################

import scapy.all as scapy
import socket

# Create an ARP request.
request = scapy.ARP() 
request.pdst = '192.168.86.1/24'

# Create an Ethernet broadcast.
broadcast = scapy.Ether()
broadcast.dst = 'ff:ff:ff:ff:ff:ff'

# Combine ARP request with Ethernet broadcast.
request_broadcast = broadcast / request

# Send the request and capture the responses.
clients = scapy.srp(request_broadcast, timeout=10, verbose=1)[0]

# Iterate over each client and print only IP and hostname.
for element in clients:
    ip = element[1].psrc
    try:
        # Try to get the hostname using reverse DNS lookup.
        hostname = socket.gethostbyaddr(ip)[0]
    except socket.herror:
        # If the hostname could not be resolved, default to 'Unknown'.
        hostname = "Unknown"
    
    # Print the IP and hostname of active devices on the network.
    print(f"{ip}\t{hostname}")

# To run the script use the command "sudo -E python main.py" in the terminal.
