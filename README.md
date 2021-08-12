# PySockets
A simple Python Sockets p2p connection system made without any extra Libraries.
tested and built on python-3.8.9

## Usage:
# Starting The Server
To Start The Server, Use The Following command:
```
>>server.py <ip> <port>
--
  Example: >>server.py localhost 1234

#------- | Example Output | ------- (Following Output is When a Host Joins The Server...)

 [+] Binded Server To >> 'localhost:1234'

====================--< Waiting For Connections >--=====================


 Connection from ('127.0.0.1', 51374) has been established!

 Upcoming Message Length: 43
 Recieved: 'add_h;My_username;6.tcp.eu.ngrok.io;17553'
 Started Wake Thread for 'My_username'....
 Current Hosts:  {'My_username': ('6.tcp.eu.ngrok.io', '17553')}

 Current Clients:  0

```
# Hosting and Adding Address to The Server:
Hosts Can add thier address to the Server by Running The Following Command:
```
>>host.py <Server_ip> <Server_port> <Host_username>
--
  Example: >>host.py localhost 1234 My_Usernmae

#------- | Example Output | ------- 
 [+] Connected To Server >> 'localhost:1234'

=========================< Host >=========================

 [+] Waiting for connections...

```

Running this command will download and run [Ngrok](https://ngrok.com/), Once The Ngrok tunnel is online the Host will send its _ngrok-address and port_ along with the user-name to the **Server** this data will be stored in a Dictionary in the Server.

# Fetching Online Hosts:
Clients can fetch addresses from the server by using this command:
```
>>join.py <Server_ip> <Server_port>
--
  Example: >>join.py localhost 1234

#------- | Example Output | ------- (Following Output is when a Host is online...)
 [+] Connected To Server >> 'localhost:1234'

=========================< Client >=========================


 Upcoming Message Length: 47
 Message: {'My_username': ['6.tcp.eu.ngrok.io', '17553']}
```

Clients will be returned the online hosts-Dictionary and will update it as soon as a host joins or leaves...


