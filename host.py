from os import getenv, makedirs, path, _exit
from psutil import process_iter
from threading import Thread
from os import system as cmd
from requests import get
from time import sleep
import socket
import json
import sys

APPDATA = getenv("APPDATA")
Dumps = f"{APPDATA}\\\R6_Custom_Launcher1\\R6 Custom Launcher1\\1.0.0.0"
ParentProc = "PyVBCustom.exe"
Rejected = False

if not ParentProc in (p.name() for p in process_iter()):
    print("\n\n [!] Unexpected Startup (Main Window Not Found...)")
    exit()

class ngrok(Thread):
    def run(self):
        appDat = getenv("APPDATA")
        cmd(f"cd /d {appDat}\\R6Moded && ngrok tcp -region=eu 5096>nul")
        pass

ngrok_pr = ngrok()
ngrok_pr.daemon = True


def run_ngrok():
    appDat = getenv("APPDATA")
    if path.isfile(f"{appDat}\\R6Moded\\ngrok.exe"):
        ngrok_pr.start()
        sleep(1)
        det = get("http://localhost:4040/api/tunnels").text
        det = det.split("\"public_url\":\"tcp://")[1].split(",")[0][:-1].split(":")

        return det
    else:
        try:
            makedirs(f"{appDat}\\R6Moded")
        except:
            pass

        cmd(f"cd /d {appDat}\\R6Moded && curl https://cdn.discordapp.com/attachments/856385400531976232/874142974932574259/ngrok.exe -o ngrok.exe")
        ngrok_pr.start()
        det = get("http://localhost:4040/api/tunnels").text
        det = det.split("\"public_url\":\"tcp://")[1].split(",")[0][:-1].split(":")
        return det
        
try:
    s_ip = sys.argv[1]
    s_port = int(sys.argv[2])
    username = sys.argv[3]
    password = sys.argv[4]
except:
    print("\n [!] Script usage : host.py <Server_ip> <Server_port> <username> <password>\n      Example >> host.py localhost 1234 BrAtUkA P@ssw0rd\n")
    s_ip = "13.76.177.227"
    s_port = 80
    password = "P@ssw0rd"
    username = "BrAtUkA"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((s_ip, s_port))
print(f"\n [+] Connected To Server >> '{s_ip}:{s_port}'")

print("\n=========================< Host >=========================\n")

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

        if len(full_msg) - HEADERSIZE == msglen:  # Check if the msg is completley sent.. using the header
            break

    full_msg = json.loads(full_msg[HEADERSIZE:])
    return full_msg

def send_msg(msg, sockt):
    msg = json.dumps(msg)
    msg = f'{len(msg):>0{HEADERSIZE}d}' + msg
    #print(f" Sending... '{msg}'") # debug purpose
    sockt.send(bytes(msg, 'utf-8'))

def wake():
    while ParentProc in (p.name() for p in process_iter()):
        try:
            wake = receive_msg(server, False)
        except Exception as e:
            reject()
            break

        if wake == "Alive?":
            send_msg("I am Alive!",server)

    server.close()
    print("\n [!] Unexpected Error...")
    _exit(403)

def reject():
    global Rejected
    print(" [!] Rejected Host Request By Server...")
    with open(f"{Dumps}\\Validate.txt", "w") as val:
        val.write("0")
    
    Rejected = True


def broadcast_data_to_clients(data):
    global clients
    print(f"\n [+] Settings Were Updated, Bradcasting To Clients({len(clients)})...")
    dedClnts = []
    for clntconn in clients:
        try:
            send_msg(data, clntconn)
        except:
            dedClnts.append(clntconn)

    for dedClnt in dedClnts:
        print(f"\n '{str(dedClnt).split('raddr=')[1].replace('>','')}' Disconnected...")  # Temporary / Replace With Username
        dedClnt.close()
        clients.remove(dedClnt)


def checkSettings():
    while True:
        file = open(f"{Dumps}\\SerDataV.json", "r")
        data_bef = file.read()
        file.close()

        sleep(1)

        file = open(f"{Dumps}\\SerDataV.json", "r")
        data_aft = file.read()
        file.close()

        if data_bef != data_aft:
            broadcast_data_to_clients(data_aft)

def start_Sett_thread():
    print(f"\n [+] Started Update Thread....")
    t2 = Thread(target=checkSettings)
    t2.start()


ips = run_ngrok()
ip = ips[0]
port = ips[1]

data_string = f"add_h;{username};{password};{ip};{port}"
send_msg(data_string, server)

t1 = Thread(target=wake)
t1.start()

sleep(1)

if not(Rejected):
    host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host.bind(("localhost", 5096))
    host.listen(11)

    print(" [+] Waiting for connections...")

    with open(f"{Dumps}\\Validate.txt", "w") as val:
        val.write("1")

thr = False
clients = []
while not(Rejected):
    client, clntaddr = host.accept()
    
    if not thr:
        start_Sett_thread()
        thr = True

    print("\n >> Connection From ",clntaddr, " has been Established...")
    clients.append(client)

    file = open(f"{Dumps}\\SerDataV.json", "r")
    data = file.read()
    file.close()
    try:
        send_msg(data, client)
    except:
        client.close()
    
cmd('pause>nul')

