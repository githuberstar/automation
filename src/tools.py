#!/usr/bin/env python
# -*- coding:utf-8 -*-

# #给server端发送命令
import socket
import traceback


def remote_exe():
    host = '192.168.19.102'
    port = 51888

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except Exception as e:
        traceback.format_exc()

    input_command = "C:\\Users\\zhujihui\\Desktop\\auto_save.exe"
    s.send(input_command.encode('utf-8'))

    # 利用shutdown()函数使socket双向数据传输变为单向数据传输
    # 该参数表示了如何关闭socket。具体为：0表示禁止将来读；1表示禁止将来写；2表示禁止将来读和写
    s.shutdown(1)


if __name__ == "__main__":
    remote_exe()
