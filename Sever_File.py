import socket,time,SocketServer,struct,os,thread
host='172.16.221.1'
port=12307
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #建立连接
s.bind((host,port)) #绑定需要监听的Ip和端口号
s.listen(1)

 
def conn_thread(connection,address):  
    while True:
        try:
            connection.settimeout(600) #设定连接超时时间
            fileinfo_size=struct.calcsize('128sl') #文件信息打包，128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小
            buf = connection.recv(fileinfo_size)
            if buf: #只要有新文件就继续传输
                filename,filesize =struct.unpack('128sl',buf) #根据128sl解包文件信息，与client端的打包规则相同 
                filename_f = filename.strip('\00')#去除文件名中的多余空字符
                filenewname = os.path.join('/Users/zx/Desktop/Mytest.txt')#文件的接收路径
                print 'file new name is %s, filesize is %s' %(filenewname,filesize) #输出接收了的文件名字及大小
                recvd_size = 0 
                file = open(filenewname,'wb') #打开文件写入接收到的内容
                print 'stat receiving...'
                while not recvd_size == filesize:#使用。recv（）方法以1024为单位读取文件
                    if filesize - recvd_size > 1024:
                        rdata = connection.recv(1024)
                        recvd_size += len(rdata)
                    else:
                        rdata = connection.recv(filesize - recvd_size) 
                        recvd_size = filesize
                    file.write(rdata)#写文件
                file.close()
                print 'receive done'
        except socket.timeout:#连接超时socket关闭
            connection.close()


while True:
    connection,address=s.accept()#取得新连接的地址及端口
    print('Connected by ',address)
    thread.start_new_thread(conn_thread,(connection,address)) #为新链接建立新的线程

s.close()
