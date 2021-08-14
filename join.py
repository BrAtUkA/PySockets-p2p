from os import system as cmd
from time import sleep
import threading
import socket
import json
import sys

try:
    s_ip = sys.argv[1]
    s_port = int(sys.argv[2])
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

def Update_hostList():
    global hosts
    while True:
        try:
            hosts = receive_msg(server, True)
        except:
            break
        print(f" Hosts = {hosts}\n\n")

    print(" [!] Unexpected Error... (Server Connection Closed)")
    exit()

t1 = threading.Thread(target=Update_hostList,)
t1.start()

while True:
    pass   # TODO: Figure out a way to specify a host... ; TODO2: Add Method to connect and comunicate with specified host

