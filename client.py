import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096  # send 4096 bytes each time step

# Owen change this ip to your computer's
host = ""
# the port, let's use 5001
port = 5003
# the name of file we want to send, make sure it exists
fileName = input("Enter the file's name: ")
# get the file size
filesize = os.path.getsize(fileName)
s = socket.socket()
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")
 # send the fileName and filesize
s.send(f"{fileName}{SEPARATOR}{filesize}".encode())

  # start sending the file
progress = tqdm.tqdm(range(
       filesize), f"Sending {fileName}", unit="B", unit_scale=True, unit_divisor=1024)
with open(fileName, "rb") as f:
    while True:
    # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
        # file transmitting is done
            break
        # we use sendall to assure transimission in
        # busy networks
        s.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
    # close the socket
    s.close()
