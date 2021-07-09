import socket
import os

os.system('clear')

HOST = '127.0.0.1' #server's hostname
PORT = 3333 #port used by the server
SIZE = 1024

def main():
  try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#creates socket object
    client_socket.connect((HOST, PORT))#connects to the server
    print('\tjoining (',HOST, '.', PORT, ')...' )
    while(True):
      try:
        print('\n\t\tMessage to the Server: ', end='') 
        inp = input()
        client_socket.sendall((inp.encode('utf-8')))#sends the message
        data = client_socket.recv(SIZE).decode()#reads the server's reply

        print('\t\tReceived from Server(',HOST, '.', PORT, ')', repr(data))#prints the server's reply
      except EOFError:
        break
    print('closing connection')

  except (ConnectionRefusedError):
    print('[Errno 111] Connection refused\n\n\n')

main()