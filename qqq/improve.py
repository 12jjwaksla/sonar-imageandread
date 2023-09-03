<<<<<<< HEAD
#请注意，请在树莓派启动的时候 将这个程序设置为自启动
import socket
import PIL
# 1.创建socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 链接服务器
server_addr = ("192.168.0.144", 7000)
tcp_socket.connect(server_addr)

# 3. 发送数据

tcp_socket.send('$GPOTH,256,*75\r\n')#发送启动声呐软件的命令

# 4. 关闭套接字
=======
#请注意，请在树莓派启动的时候 将这个程序设置为自启动
import socket
import PIL
# 1.创建socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 链接服务器
server_addr = ("192.168.0.144", 7000)
tcp_socket.connect(server_addr)

# 3. 发送数据

tcp_socket.send('$GPOTH,256,*75\r\n')#发送启动声呐软件的命令

# 4. 关闭套接字
>>>>>>> b8368ea (tijiao)
tcp_socket.close()