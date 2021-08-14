from os import system as cmd
from requests import get
from time import sleep
import threading
import socket
import json
import sys
import os

class ngrok(threading.Thread):
    def run(self):
        appDat = os.getenv("APPDATA")
        cmd(f"cd /d {appDat}\\R6Moded && ngrok tcp -region=eu 1234>nul")
        pass

ngrok_pr = ngrok()
ngrok_pr.daemon = True


def run_ngrok():
    appDat = os.getenv("APPDATA")
    if os.path.isfile(f"{appDat}\\R6Moded\\ngrok.exe"):
        ngrok_pr.start()
        sleep(2)
        det = get("http://localhost:4040/api/tunnels").text
        det = det.split("\"public_url\":\"tcp://")[1].split(",")[0][:-1].split(":")

        return det
    else:
        try:
            os.makedirs(f"{appDat}\\R6Moded")
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
    username = "BrAtUkA"
    password = "P@ssw0rd"


ips = run_ngrok()
ip = ips[0]
port = ips[1]



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

data_string = f"add_h;{username};{password};{ip};{port}"
send_msg(data_string, server)


def wake():
    while True:
        try:
            wake = receive_msg(server, False)
        except Exception as e:
            print(" [!] Rejected Host Request By Server...")
            break

        if wake == "Alive?":
            send_msg("I am Alive!",server)
    exit()

t1 = threading.Thread(target=wake)
t1.start()

host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host.bind(("localhost", int(port)))
host.listen(11)

print(" [+] Waiting for connections...")

while True:
    client, clntaddr = host.accept()
    # TODO: Figure out a way to specify Mods/To be synced values... ; TODO2: Add Method to connect and comunicate with clients


cmd('pause>nul')

