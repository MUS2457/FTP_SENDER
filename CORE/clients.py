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
        
    def delete_file(self, file_name) :
        if self.ftp is None :
            return "not connected"
        
        current_dir = self.ftp.pwd()  

        user = input(f"Are you sure you want to delete {file_name} from the path {current_dir} ? (y/n) ").strip().lower()

        if user == "y" :

            try :
                self.ftp.delete(file_name)
                return f"The file {file_name} has been deleted "
            
            except ftplib.error_perm :
                return f"Permission denied or file not found: {file_name}"
    
        return "Deletion has been cancelled"
    

    def rename_file(self, path) :
        if self.ftp is None :
            return "not connected"
        
        old_name = os.path.basename(path)
        _, ext = os.path.splitext(old_name)
        file_path = os.path.dirname(path)

        validation = input(f"Are you sure you want to rename this file {old_name} from path {path}? (y/n)").strip().lower()

        if validation == "y" :
            
            name = input("Enter new name for the file without the extention").strip()
            new_name = name + ext
            new_path = os.path.join(file_path, new_name)
            try :
                self.ftp.rename(old_name, new_name)
                return f"{old_name} has been renamed to {new_name} (new path: {new_path})"

            except ftplib.error_perm :
                return f"Permission denied or file not found: {old_name}"
            
        return "Renaming has been cancelled"
        
    def info_items(self):
        if self.ftp is None:
            return "not connected"

        try:
            raw = []
            self.ftp.retrlines("LIST", raw.append) # genarator of lines == yield

            items = []
            for line in raw:
            # detect type cause the line is start with d == dir or - == file
                item_type = "dir" if line.startswith("d") else "file"

            # extract name (last token)
                name = line.split()[-1]

                items.append({
                "name": name,
                "type": item_type
                })

            return items

        except ftplib.all_errors:
            return "access denied from the server"
    
    def current_path(self) :
        if self.ftp is None :
            return "not connected"
        
        return self.ftp.pwd()