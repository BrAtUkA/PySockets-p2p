# PySockets
A simple Python Sockets p2p connection system (designed for Rainbow Six mods)

## Usage:
To Start The Server, Use The Following command:
```
>>server.py <ip> <port>
```

Hosts Can Join this Server by Running The Following Command:
```
>>host.py <Server_ip> <Server_port> <Host_username>
```
Running this command will download and run [Ngrok](https://ngrok.com/), Once The Ngrok tunnel is online the Host will send its _ngrok-address and port_ along with the user-name to the **Server** this data will be stored in a Dictionary in the Server.

Clients can fetch addresses from the server by using this command:
```
>>join.py <Server_ip> <Server_port>
```

Clients will be returned the online hosts-Dictionary and will update it as soon as a host joins or leaves...


