import connectfour
import socket


host = 'circinus-32.ics.uci.edu'
port = 5151
inp = 'I32CFSP_HELLO Gary'

connection_socket = socket.socket()
connection_socket.connect((host, port))
if connection_socket.connect((host, port)) is False:
    print('Connected')

connection_socket.close()
