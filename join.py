from os import getenv, _exit, remove
from psutil import process_iter 
from time import sleep
import threading
import socket
import json
import sys

APPDATA = getenv("APPDATA")
Dumps = f"{APPDATA}\\\R6_Custom_Launcher1\\R6 Custom Launcher1\\1.0.0.0"
ParentProc = "PyVBCustom.exe"

if not ParentProc in (p.name() for p in process_iter()):
    print("\n\n [!] Unexpected Startup (Main Window Not Found...)")
    exit()

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
with open(f"{Dumps}\\SerDataP.json", "w") as file:
    file.write("{}")

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

def watchParentProc():
    while True:
        if not ParentProc in (p.name() for p in process_iter()):
            print(" [!] Unexpected Error...")
            server.close()
            _exit(404)
        sleep(2)

def updateHostlist(Hlis):
    global hosts
    hosts = Hlis
    print(f" Hosts = {hosts}\n\n")

    with open(f"{APPDATA}\\\R6_Custom_Launcher1\\R6 Custom Launcher1\\1.0.0.0\\CurrentHosts.json", "w") as data:
        data.write(json.dumps(hosts))

def watch_data():
    while True:
        with open(f"{Dumps}\\SerDataP.json", "r") as file:
            data_bef = file.read()

        sleep(2)

        with open(f"{Dumps}\\SerDataP.json", "r") as file:
            data_aft = file.read()

        if data_bef != data_aft:
            protect_Data()

def protect_Data():
    print(" [+] Updated Data...")
    global data
    with open(f"{Dumps}\\SerDataP.json", "w") as file:
        file.write(json.dumps(data))
    

t1 = threading.Thread(target=watchParentProc)
t1.start()

t2 = threading.Thread(target=Recieve_hostList)
t2.start()

t3 = threading.Thread(target=watch_data)
t3.start()

sleep(1)

Connected = False
print(" [!] Waiting For Selection...")
while True:
    if not(Connected):
        try:
            with open(f"{Dumps}\\SelectedHost.txt", "r") as hName:
                hName = hName.read()
            host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host.connect((hosts[hName][0], int(hosts[hName][1])))
            print(f"\n >> Connected to {hName}...")
            remove(f"{Dumps}\\SelectedHost.txt")

            with open(f"{Dumps}\\conn.txt", "w") as conn:
                conn.write("1")
                
            Connected = True
        except Exception as e:
            pass
        sleep(1)

    while Connected:
        try:
            data = receive_msg(host, False)
            data = json.loads(data)
            #print("\n\n",data, "\n\n")
            with open(f"{Dumps}\\SerDataP.json", "w") as file:
                file.write(json.dumps(data))

        except Exception as e:
            print(f"\n >> Disconnected From '{hName}'...")
            print(" [!] Waiting For Selection...")
            host.close()
            Connected = False


