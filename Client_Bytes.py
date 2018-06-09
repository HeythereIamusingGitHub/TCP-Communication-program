import socket
import sys


def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('172.16.221.129 ', 6666))    #创建 socket连接到虚拟机服务器，端口6666
    except socket.error as msg:
        print msg
        sys.exit(1)#创建socket失败处理
    print s.recv(1024)#输出从Sever传来的交互信息
    while 1:
        data = raw_input('please input words: ')#输入要传送的文字
        s.send(data)#发送数据
        print s.recv(1024)#输出服务器发送的交互信息
        if data == 'exit':
            break
    s.close()#关闭 socket


if __name__ == '__main__':
    socket_client()
