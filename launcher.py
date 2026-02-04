import subprocess
import sys
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLIENT_PATH = os.path.join(BASE_DIR, "client", "client.py")

def git_pull():
    subprocess.call(["git", "pull"], cwd=BASE_DIR)

while True:
    try:
        git_pull()

        p = subprocess.Popen(
            [sys.executable, CLIENT_PATH],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        p.wait()
        time.sleep(3)

    except Exception:
        time.sleep(5)
