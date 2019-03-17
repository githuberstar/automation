#!/usr/bin/env python
# -*- coding:utf-8 -*-

# #执行客户端发送过来的命令，并把执行结果返回给客户端
import socket, traceback, subprocess
import os

host = ''
port = 51888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host, port))
s.listen(1)

while 1:
    try:
        client_socket, client_addr = s.accept()
    except Exception as e:
        traceback.print_exc()
        continue

    try:
        print('From host:', client_socket.getpeername())
        while 1:
            command = client_socket.recv(4096)
            if not len(command):
                break
            print(client_socket.getpeername()[0] + ':' + str(command))

            # 执行客户端传递过来的命令
           # handler = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            handler = os.system(command.decode('utf-8'))
            output = handler.stdout.readlines()
            if output is None:
                output = []

            for one_line in output:
                client_socket.sendall(one_line)
                client_socket.sendall("\n")

            client_socket.sendall("ok")

    except Exception as e:
        traceback.print_exc()

    try:
        client_socket.close()
    except Exception as e:
        traceback.print_exc()
