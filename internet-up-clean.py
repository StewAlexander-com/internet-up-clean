#!/usr/bin/env python3
import os
import sys
import uuid
import socket

#Store the socket hostname and IP address in variables
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

#Store the ip address 8.8.8.8 to a variable called Google
Google = "8.8.8.8"

#Store the variable Google in a list called hosts
hosts = [Google]


# for host in hosts ping 3 times
for host in hosts:
    response = os.system("ping -c 3 " + host)
    if response == 0:
        print ("\nPlease copy the below to an email \nand send it to the Network Administrator\n")
        #print a line to the screen
        print ("\n===================================\n")
        print("The  Internet is up!")
        #print the hostname
        print ("Hostname: " + hostname)
        # Print the MAC Address of the network interface
        print ("The MAC address is: ", end="")
        print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
        for ele in range(0,8*6,8)][::-1]))
        #print a line to the screen
        print ("\n===================================\n")
    else:
         print ("\nPlease copy the below to an email \nand send it to the Network Administrator\n")
         #print a line to the screen
         print ("\n===================================\n")
         print("The Internet is down!")
        #print the hostname
         print ("Hostname: " + hostname)
        # Print the MAC Address of the network interface
         print ("The MAC address is: ", end="")
         print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
         for ele in range(0,8*6,8)][::-1]))
         #print a line to the screen
         print ("\n===================================\n")

