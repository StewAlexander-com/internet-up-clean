# internet-up-clean
Simple program for a user to provide networking details to the network admin(s)
## Output:
----
```
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=116 time=28.9 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=116 time=23.4 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=116 time=23.9 ms

--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2004ms
rtt min/avg/max/mdev = 23.438/25.397/28.858/2.453 ms

Please copy the below to an email 
and send it to the Network Administrator

===================================

The  Internet is up!
Hostname: <hostname>
The MAC address is: <MAC Address>

===================================
```
<br>
* If the network is down it says so and still provides the hostname and the MAC address for the Network Admin
