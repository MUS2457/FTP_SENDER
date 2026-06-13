import ftplib

class FTPClient:
    def __init__(self, host,port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.ftp = ftplib.FTP()
    
    def connect(self) :
        self.ftp.connect(self.host, self.port)

    def login(self)
    