import socket,os,struct
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('172.16.221.1',12307))
while True:    
    filepath = raw_input('Please Enter chars:\r\n')
    if filepath == 'bye':
        break
    if os.path.isfile(filepath):
        fileinfo_size=struct.calcsize('128sl')
        fhead = struct.pack('128sl',os.path.basename(filepath),os.stat(filepath).st_size)
        s.send(fhead) 
        print 'client filepath: ',filepath
        fo = open(filepath,'rb')
        while True:
            filedata = fo.read(1024)
            if not filedata:
                break
            s.send(filedata)
        fo.close()
        print 'send over...'