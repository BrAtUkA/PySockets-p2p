from os import getenv, _exit, remove
from psutil import process_iter 
from time import sleep
import threading
import socket
import json
import sys

APPDATA = getenv("APPDATA")
Dumps = f"{APPDATA}\\HostJoinSys"
ParentProc = "PythonHostJoinAPI.exe"

if not ParentProc in (p.name() for p in process_iter()):
    print("\n\n [!] Unexpected Startup (Main Window Not Found...)")
    exit()

try:
    s_ip = sys.argv[1]
    s_port = int(sys.argv[2])
    uName = sys.argv[3]
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

with open(f"{Dumps}\\DisV.txt", 'w') as file2:
    file2.write("")

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

    with open(f"{Dumps}\\CurrentHosts.json", "w") as data:
        data.write(json.dumps(hosts))

def watch_data():
    while True:
        with open(f"{Dumps}\\SerDataP.json", "r") as file:
            data_bef = file.read()

        sleep(1)

        with open(f"{Dumps}\\SerDataP.json", "r") as file:
            data_aft = file.read()

        if data_bef != data_aft:
            protect_Data()

def protect_Data():
    global data
    writ = False
    while not writ:
        try:
            with open(f"{Dumps}\\SerDataP.json", "w") as file:
                file.write(json.dumps(data))

            writ = True
            print(" [+] Updated Data...")
            
            with open(f"{Dumps}\\updated.txt", "w") as ch:
                ch.write("1")
        except:
            print(" [!] Write Data Exception! (Retrying...)")
            sleep(0.05)
    
def Diss():
    while True:
        try:
            with open(f"{Dumps}\\DisV.txt", 'r') as DisV:
                DisV = DisV.read()
        except:
            pass

        if DisV == "Now":
            DisV = ""
            Disconnect()
        sleep(1)

def Disconnect():
    global Connected
    global host
    global data
    if Connected:
        print(f"\n >> Disconnected From '{hName}'...")

        with open(f"{Dumps}\\Dis.txt","w") as dis:
            dis.write("4O4")
        try:
            remove(f"{Dumps}\\DisV.txt")
            print(" >> User Interrupt...")
        except:
            print(" >> Host Connection Lost...")
            print("\n [!] Waiting For Selection...")

        data = {}
        host.close()
        Connected = False

t1 = threading.Thread(target=watchParentProc)
t1.start()

t2 = threading.Thread(target=Recieve_hostList)
t2.start()

t3 = threading.Thread(target=watch_data)
t3.start()

t4 = threading.Thread(target=Diss)
t4.start()

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
            send_msg(uName,host)

            with open(f"{Dumps}\\connected.txt", "w") as conn:
                conn.write("1")

            Connected = True
        except Exception as e:
            pass

        sleep(1)

    while Connected:
        try:
            data = receive_msg(host, False)
            print("\n\n",data, "\n\n")
            if isinstance(data, str):
                data = json.loads(data)

            writ = False
            while not writ:
                try:
                    with open(f"{Dumps}\\SerDataP.json", "w") as file:
                        file.write(str(data))
                    writ = True
                except:
                    print(" [!] Write Data Exception! (Retrying...)")
                    sleep(0.05)

        except Exception as e:
            Disconnect()


