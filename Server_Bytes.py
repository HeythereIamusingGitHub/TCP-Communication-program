import socket
import threading
import time
import sys


def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('172.16.221.1', 6666))#创建 socket，端口6666
        s.listen(10)#最多允许10个连接并发
    except socket.error as msg:#连接错误处理
        print msg
        sys.exit(1)
    print 'Waiting connection...'

    while 1:
        conn, addr = s.accept()#取得新连接的地址及端口
        t = threading.Thread(target=deal_data, args=(conn, addr))#为新的链接创建新线程
        t.start()#启动新线程

def deal_data(conn, addr):
    print 'Accept new connection from {0}'.format(addr)
    conn.send('Hi, Welcome to the server!')#向Client发送交互信息
    while 1:
        data = conn.recv(1024)#接收Client传来的信息
        print '{0} client send data is {1}'.format(addr, data)#输出Client传来的信息
        if data == 'exit' or not data:#若信息为Exit或没有信息时关闭连接
            print '{0} connection close'.format(addr)
            conn.send('Connection closed!')
            break
        conn.send('Received words is {0}'.format(data))#向Client发送Sever接收到的信息
    conn.close()


if __name__ == '__main__':
    socket_service()
    
     #Contributed by 许焯 信息16-2
