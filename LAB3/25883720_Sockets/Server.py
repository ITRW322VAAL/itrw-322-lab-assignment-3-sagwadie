#!/usr/bin/env python3

import socket
HOST='127.0.0.1' #Standart loopback interface address (localhost)
PORT=9999 #Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn,addr=s.accept()
    with conn:
         print('Server is conneccted with address', addr)
         while True:
              data=conn.vecv(2048) #default byte stream size
              if nor data:
                  break
              conn.sendall(data)