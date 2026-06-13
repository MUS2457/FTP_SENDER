import ftplib
import os

class FTPClient:
    def __init__(self, host,port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.ftp = None
    
    
    def connect(self) :
        self.ftp = ftplib.FTP()
        self.ftp.connect(self.host, self.port)

    def login(self) :
        if self.ftp is None :
            return "not connected"
        
        elif self.username == self.password == "" :
            self.ftp.login()

        else :
            self.ftp.login(self.username, self.password)
    
    def list_files(self) :
        if self.ftp is None :
            return "not connected"
        
        try :
            return self.ftp.nlst()
        
        except ftplib.all_errors :
            return "access denied from the server"
        
    def change_directory(self, path) :
        if self.ftp is None :
            return "not connected"
        
        try :
            passing = self.ftp.cwd(path)  # return None in succes
            return "you are in the chosen part"
        
        except ftplib.all_errors :
            return "access denied from the server"
        
    def upload_file(self, path) :
        if self.ftp is None :
            return "not connected"
        
        if os.path.exists(path) :
            file_name = os.path.basename(path)
            try :
                with open (path, "rb") as file :
                    self.ftp.storbinary(f"STOR {file_name}", file) # i can increase speed by increasing th size of the chunk(df = 8kb)
                                                                    #  can be only x >= 1 in  (STOR {file_name}, file, x * 1024) X is in kb
                    return "file uploaded successfully" 

            except OSError :
                return "local file cannot be opened (not found, permission denied, or other OS error)"
            
            except ftplib.all_errors :
                return "upload failed , the server rejected the file"
            
        else :
            return f"the path : **{path}** , does not exist "
        
    def dowload_file(self, path) :
        if self.ftp is None :
            return "not connected"
        
        file_name = os.path.basename(path)

        try :
            with open(path, "wb") as down :
                self.ftp.retrbinary(f"RETR {file_name}",down.write, 128*1024)

                return "file has been dowloaded succesfuly"
        
        except OSError:
            return "local file cannot be created (permission denied, invalid path, or disk error)"
        
        except ftplib.all_errors :
            return "download failed, the server rejected the request or file does not exist"