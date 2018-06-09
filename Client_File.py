import socket,os,struct
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('172.16.221.1',12307))#创建连接至由guest os和Host os 组成的Vnet中Host的IP地址绑定需要监听的端口
while True:    
    filepath = raw_input('Please Enter chars:\r\n')#输入要上传的文件路径
    if filepath == 'bye':
        break
    if os.path.isfile(filepath):
        fileinfo_size=struct.calcsize('128sl')#定义文件信息打包规则，128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小，
        fhead = struct.pack('128sl',os.path.basename(filepath),os.stat(filepath).st_size)#打包文件
        s.send(fhead) #发送文件信息
        print 'client filepath: ',filepath #输出文件路径
        fo = open(filepath,'rb')
        while True:
            filedata = fo.read(1024)  #打开文件并读取文件内容
            if not filedata:
                break
            s.send(filedata) #传送文件内容
        fo.close() #关闭Socket连接
        print 'send over...'

        
        Contributed by 许焯 信息16-2
