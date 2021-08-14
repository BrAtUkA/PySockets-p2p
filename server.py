CMD = False
import os
if os.name == 'nt':
    from os import system as cmd
    CMD = True
    
from time import sleep, time
import threading
import socket
import json
import sys


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

        if len(full_msg) - HEADERSIZE == msglen:  # Check if the msg is completley sent.. using the header
            break

    full_msg = str(json.loads(full_msg[HEADERSIZE:]))
    return full_msg

def send_msg(msg, sockt:socket.socket):
    msg = json.dumps(msg)
    msg = f'{len(msg):>0{HEADERSIZE}d}' + msg
    #print(f" Sending... '{msg}'")
    sockt.send(bytes(msg, 'utf-8'))


def check_host(host, hostip, conn):
    while True:
        sleep(2)
        try:
            send_msg("Alive?", conn)
            wake = receive_msg(conn, False)
            if wake != "I am Alive!":
                raise Exception
        except:
            rem_host(host, hostip)
            print(f" Host '{host}' Has Ended Game...")
            return

def start_wake_thread(host, hostip, conn):
    print(f" Started Wake Thread for '{host}'....")
    t1 = threading.Thread(target=check_host, args=(host, hostip, conn))
    t1.start()


def broadcast_hosts_to_clients():
    print(" Current Hosts: ",len(hosts),"\n")
    for clntconn in clntconns:
        clntconn:socket.socket
        try:
            send_msg(hosts, clntconn)
        except:
            clntconn.close()
            clntconns.remove(clntconn)
    print(" Current Clients: ",len(clntconns),"\n")


def add_host(host, hostaddr, hostport, hostip, conn):
    global hosts
    if hostip in hostconns:
        return False 
    else:
        hostconns.add(hostip)
        hosts[host] = (hostaddr, hostport)
        start_wake_thread(host, hostip, conn)
        broadcast_hosts_to_clients()
        return True

def rem_host(host, hostip):
    global hosts
    hosts.pop(host, None)
    hostconns.remove(hostip)
    broadcast_hosts_to_clients()

def valid_host(host, hostpass, hostip:str):
    global Hconn_attempts
    with open("whitelist.json", "r") as validHosts:
        validHosts = json.loads(validHosts.read())

    try:
        if validHosts[host] == hostpass:
            Hconn_attempts[hostip] = 0
            return True
        else:
            raise Exception
    except:
        return False



def add_client(conn:socket.socket):
    global hosts
    try:
        send_msg(hosts, conn)
    except:
        conn.close()
    else:
        clntconns.append(conn)
    print(" Current Clients: ",len(clntconns),"\n")

    
# Black Listing / Removing...
def track_Hconns(hostip:str):
    global Hconn_attempts
    try:
        if Hconn_attempts[hostip] >= MAXINVLREQ-1:
            Bl_file = open("blacklist.json", "r")
            Bl = json.loads(Bl_file.read())
            Bl[str(hostip)] = time()
            Bl_file.close()

            Bl_file = open("blacklist.json", "w")
            Bl_file.write(json.dumps(Bl))
            Bl_file.close()

        else:
            Hconn_attempts[hostip] += 1 
    except Exception as e:
        Hconn_attempts[hostip] = 1

def reject_blHost(hostip:str):
    refresh_blacklist(hostip)
    
    global Hconn_attempts

    with open("blacklist.json", "r") as Bl:
        Bl = json.loads(Bl.read())

    if hostip in Bl:
        print(" Blacklisted Request Recieved, Rejected...")
        return True
    else:
        return False

def refresh_blacklist(hostip):
    Bl_file = open("blacklist.json", "r")
    Bl = json.loads(Bl_file.read())
    Bl:dict
    Bl_file.close()

    try:
        if time() - Bl[hostip] >= BLLTIMEOUT:
            Hconn_attempts[hostip] = 0   
            Bl.pop(hostip, None)
            Bl_file = open("blacklist.json", "w")
            Bl_file.write(json.dumps(Bl))
            Bl_file.close()
            print(f" Removed {hostip} From Blacklist...")
        else:
            print(f" Time Remaining For {hostip} = {round((BLLTIMEOUT-(time() - Bl[hostip]))/60, 2)} mins..")
    except:
        pass


def update_title():
    global clntconns
    global hosts
    if CMD:
        cmd(f'title Server : Total Client Connects: {len(clntconns)} : Online Hosts: {len(hosts)}')

# ---- main -----

HEADERSIZE = 20
BLLTIMEOUT = 3600  # seconds
MAXINVLREQ = 10

try:
    s_ip = sys.argv[1]
    s_port = int(sys.argv[2])
except:
    print("\n [!] Script usage : server.py <Server_ip> <Server_port>\n     Example >> server.py localhost 1234\n")
    s_ip = "10.1.1.4"
    s_port = 80

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((s_ip, s_port))
print(f"\n [+] Binded Server To >> '{s_ip}:{s_port}'")
print("\n====================--< Waiting For Connections >--=====================\n")
server.listen(512)

hosts = dict()
hostconns = set()
clntconns = list()
Hconn_attempts = dict()

while True:
    conn, hostip = server.accept()
    print(f"\n Connection from {hostip} has been established!")
    try:
        x = receive_msg(conn, True)
        print(f" Recieved: '{x}'")
        cmnds = x.split(";")
    except:
        conn.close()
        continue

    cmnd = cmnds[0]
    host = cmnds[1]

    if cmnd == "add_h" and len(cmnds)==5:
        if reject_blHost(hostip[0]):
            conn.close()
            continue

        hostpass = cmnds[2]
        hostaddr = cmnds[3]
        hostport = cmnds[4]
        if valid_host(host, hostpass, hostip[0]):
            add_host(host, hostaddr, hostport, hostip[0], conn)
        else:
            track_Hconns(hostip[0])

            print(" Unauthorized Host Connection attempt, Rejected...")
            print(f" Total Rejected : {Hconn_attempts[hostip]}")
            conn.close()

    elif cmnd == "add_c" and len(cmnds)==2:
        add_client(conn)
    else:
        conn.close()
