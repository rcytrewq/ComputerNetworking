from _thread import start_new_thread #work with multiple threads
                                     #multiple simultaneous clients
import socket
import os

os.system('clear')

HOST = '127.0.0.1'
PORT = 3333
SIZE = 1024

numberOfClients=0



def client_communication(address, connection):
  print('\n\t',address,'   connected...')
  # print('---------------------------------')
  # print(clientsAddresses)
  # print('---------------------------------')
  while(True):
    data = connection.recv(SIZE).decode() #reads data sent by client
    if (not data): break #if recv receives an empty data, closes connection
    print('\n\t\treceived from [', address[0],'.',address[1],'] ', data)
    connection.sendall(data.encode('utf-8')) #echoes data back
    print('\t\tsent to [', address[0],'.',address[1],'] ', data,'\n')
  connection.close()
  print('\n\tclosing connection ', address,'...')
  clientsAddresses.remove(address)
  clientsConnections.remove(connection)
  # print('###################################')
  # print(clientsAddresses)
  # print('###################################')
  global numberOfClients
  numberOfClients-=1


clientsAddresses = []
clientsConnections = []



def main():
  global numberOfClients
  try:
    #create a socket object
    #AF_INET -> internet adress family for IPv4
    #SOCK_STREAM -> socket type for TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('trying to connect...\n') 
    while(True):
      try: 
        server_socket.bind((HOST,PORT)) #associate the socket with a specific network interface and port number
        #IPv4 -> 2-tuple : (HOST, PORT)
        break
      except OSError:
        os.system('clear')
        print('[OSError] Address already in use\nretrying...\n')

    print('\nSERVER [', HOST,'.',PORT,']')
    server_socket.listen(1)#enables the server to accept connections
    while(True):
      

      connection, address = server_socket.accept()# blocks and waits for an incoming connection
      #returns a tuples (host, port) holding the adress of client
      numberOfClients+=1
      clientsAddresses.append(address)
      clientsConnections.append(connection)
      start_new_thread(client_communication, (clientsAddresses[numberOfClients-1], clientsConnections[numberOfClients-1]))

      if (len(clientsConnections)==0): break

  except (KeyboardInterrupt):
    print('\nexiting server...\n\n\n\n')
    



main()