# PySockets p2p System
A simple Python Sockets p2p network system made without any extra Libraries.
tested and built on python-3.8.9

## Requirements:
 - Python-3.8=< (Recommended)
 - [Ngrok](https://ngrok.com/) Account (For Hosts who can't port-forward)

## Setup:
Hosts Will have to create a [Ngrok](https://ngrok.com/) Account (So That They can accept connections from clients, without _port-forwarding_)
 - Alternatively You can also use the **ngrok account** to deploy the server without _port-forwarding_, Note that only **one tunnel** can be created with a **_free account_**.

1. Goto [Ngrok Signup](https://dashboard.ngrok.com/signup) and Create an Account.
2. Then Download The [Ngrok Exe](https://dashboard.ngrok.com/get-started/setup) From the Website.
3. Then in the dashboard goto [Your Authtoken](https://dashboard.ngrok.com/get-started/your-authtokenv) and Run The **auth** Command in the same directory as the exe:
    Example:
```
ngrok authtoken 2l7lYB2bz6uhuA3q2l3giTeLt90_48E1fNcV37hKqjprfP225
--

#------ | Successfull Authentication Output | ------
C:\Users\<username>ngrok authtoken 2l7lYB2bz6uhuA3q2l3giTeLt90_48E1fNcV37hKqjprfP225
Authtoken saved to configuration file: C:\Users\<username>/.ngrok2/ngrok.yml
```

# Usage:

## Starting The Server
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
This will Bind the Server To The Given ip and port, This Will Listen For Incoming Requests from both Hosts and Clients, and manage Data Accordingly

## Hosting and Adding Address to The Server:
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

Running this command will **download and run** [Ngrok](https://ngrok.com/), Once The Ngrok tunnel is online the Host script will send the _ngrok-address and port_ along with the username to the **Server** this data will be stored in a Dictionary in the Server.

## Fetching Online Hosts:
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


