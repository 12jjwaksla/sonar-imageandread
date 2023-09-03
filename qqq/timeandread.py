# -*- coding: UTF-8 -*-
from datetime import datetime
import socket
import binascii
import struct
server_ip = '127.0.0.1'
server_port = 7009
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))# 绑定服务器的 IP 地址和端口号
NowOnTxt = datetime.strftime(datetime.now(),'%m-%d %H:%M:%S')
now=datetime.strftime(datetime.now(),'%m%d %H%M%S')#当前时间
fname=now+'image.txt'#生成文件
#with open(fname,'a') a是追加 w是覆盖
print('open the file!')
while True:
    data, client_address = server_socket.recvfrom(5000000)#缓冲区目前不知道大小，只能往大了设定
    data1=binascii.hexlify(data)#转为16进制，但是这里是以byte类型显示的，两个16进制数拼成一个byte
    with open(fname,'a') as f:#向文件里写入数据
        f.write(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))+' '+data1+'\n')