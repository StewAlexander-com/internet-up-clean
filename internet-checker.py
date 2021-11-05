#!/usr/bin/env python3
import os
import sys
import uuid
import socket
import time

IPList =[]

#Store the socket hostname and IP address in variables
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

#Store the ip address 8.8.8.8 to a variable called Google
Google = "8.8.8.8"

#Store the variable Google in a list called hosts
hosts = [Google]

IPList = socket.gethostbyname_ex(socket.gethostname())[-1]

#ANSI color sequences for colored text results in printed statements
class bcolors:
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"


# for host in hosts ping 3 times
for host in hosts:
    response = os.system("ping /n 3 " + host)
    #Print in yellow to the screen, please reboot your computer before contacting support
    print(bcolors.YELLOW +'''\n\n    ┌──────────────────────────────────┐
    │  Please be sure to reboot your   │
    │  computer before contacting      │
    │  us at support                   │
    └──────────────────────────────────┘'''+bcolors.END)
    if response == 0:
        print ("\nPlease provide the below in \"" +bcolors.LIGHT_RED +  "====" +bcolors.END + "\" to the Network Administrators:")
        print(">"+ bcolors.LIGHT_GREEN +"\"<admin #1> \"" +bcolors.END + ", & or" + bcolors.LIGHT_GREEN + " \"<admin #2>\"\n\n"+bcolors.END)
        print("(Either by taking a picture of it with your phone,\n sending via email, by calling ext \"<ext #1>\" and or \"<ext #2>\",\n or by other means)\n")
        #print a line to the screen
        print (bcolors.LIGHT_RED + "\n===================================\n"+bcolors.END)
        print("The  Internet is up!")
        #print the IP list
        print ("The IP list is:",IPList)
        #print the hostname
        print ("Hostname: " + hostname)
        # Print the MAC Address of the network interface
        print ("The MAC address is: ", end="")
        print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
        for ele in range(0,8*6,8)][::-1]))
        #print a line to the screen
        print (bcolors.LIGHT_RED +"\n===================================\n"+bcolors.END)
    else:
         print ("\nPlease provide the below in \"" +bcolors.LIGHT_RED +  "====" +bcolors.END + "\" to the Network Administrators:")
         print(">"+ bcolors.LIGHT_GREEN +"\"<admin #1> \"" +bcolors.END + ", & or" + bcolors.LIGHT_GREEN + " \"<admin #2>\"\n\n"+bcolors.END)
         print("(Either by taking a picture of it with your phone,\n sending via email, by calling ext \"<ext #1>\" and or \"<ext #2>\",\n or by other means)\n")
         #print a line to the screen
         print (bcolors.LIGHT_RED +"\n===================================\n"+bcolors.END)
         print("The Internet is down!")
        #print the IP list
         print ("The IP list is:",IPList)
        #print the hostname
         print ("Hostname: " + hostname)
        # Print the MAC Address of the network interface
         print ("The MAC address is: ", end="")
         print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
         for ele in range(0,8*6,8)][::-1]))
         #print a line to the screen
         print (bcolors.LIGHT_RED +"\n===================================\n"+bcolors.END)

#Pausing waiting for the user to press enter to quit...
print("Press enter to quit")
quit =input()
time.sleep(0.7)
    
#Exit the program
sys.exit()
    
