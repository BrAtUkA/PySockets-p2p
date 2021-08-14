from os import system as cmd
from time import sleep
import threading
import socket
import json
import sys

try:
    s_ip = sys.argv[1]
    s_port = int(sys.argv[2])
    #hName = sys.argv[3]
except:
    print("\n [!] Script usage : join.py <Server_ip> <Server_port>\n      Example >> join.py localhost 1234\n")
    s_ip = "13.76.177.227"
    s_port = 80


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((s_ip, s_port))
print(f"\n [+] Connected To Server >> '{s_ip}:{s_port}'")

print("\n=========================< Client >=========================\n")

HEADERSIZE = 20

def receive_msg(sockt:socket.socket, Len:bool):
    full_msg = ""
    new_msg = True
    while True:
        msg = sockt.recv(24)
        
        if new_msg:
            if Len:
                print(f"\n Upcoming Message Length: {int(msg[:HEADERSIZE])}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        
        full_msg += msg.decode("utf-8")

        if len(full_msg) - HEADERSIZE == msglen:
            break

    full_msg = json.loads(full_msg[HEADERSIZE:])
    return full_msg

def send_msg(msg, sockt:socket.socket):
    msg = json.dumps(msg)
    msg = f'{len(msg):>0{HEADERSIZE}d}' + msg
    #print(f" Sending... '{msg}'")
    sockt.send(bytes(msg, 'utf-8'))

send_msg("add_c;null", server)

def Recieve_hostList():
    while True:
        try:
            hosts = receive_msg(server, True)
        except:
            break
        updateHostlist(hosts)

    print(" [!] Unexpected Error... (Server Connection Closed)")
    exit()

def updateHostlist(Hlis):
    global hosts
    hosts = Hlis
    print(f" Hosts = {hosts}\n\n")

t1 = threading.Thread(target=Recieve_hostList)
t1.start()

sleep(1)

# host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host.connect((hosts[hName][0], int(hosts[hName][1])))
                                                             # TODO: Figure out a way to specify a host [76] [11]... ; TODO2: Add Method to connect and comunicate with specified host
while True:
    # ms = receive_msg(host, True)
    # print(" Message = ", ms )
    pass                                                       

