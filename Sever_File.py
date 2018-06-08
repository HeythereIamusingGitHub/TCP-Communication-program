import socket,time,SocketServer,struct,os,thread
host='172.16.221.1'
port=12307
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(1)

 
def conn_thread(connection,address):  
    while True:
        try:
            connection.settimeout(600)
            fileinfo_size=struct.calcsize('128sl') 
            buf = connection.recv(fileinfo_size)
            if buf:
                filename,filesize =struct.unpack('128sl',buf) 
                filename_f = filename.strip('\00')
                filenewname = os.path.join('/Users/zx/Desktop/Mytest.txt')
                print 'file new name is %s, filesize is %s' %(filenewname,filesize)
                recvd_size = 0 
                file = open(filenewname,'wb')
                print 'stat receiving...'
                while not recvd_size == filesize:
                    if filesize - recvd_size > 1024:
                        rdata = connection.recv(1024)
                        recvd_size += len(rdata)
                    else:
                        rdata = connection.recv(filesize - recvd_size) 
                        recvd_size = filesize
                    file.write(rdata)
                file.close()
                print 'receive done'
        except socket.timeout:
            connection.close()


while True:
    connection,address=s.accept()
    print('Connected by ',address)
    thread.start_new_thread(conn_thread,(connection,address)) 

s.close()