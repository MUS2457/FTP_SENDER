import ftplib
import os
from CORE.helper import loading_bar_animation

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
        
    def upload_file_v1(self, path) :
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
        
    def dowload_file_v1(self, path) :
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
        
        try :
            return self.ftp.pwd()
        
        except ftplib.all_errors :
            return "access denied from the server"
    
    def file_size(self, file_name) :
        if self.ftp is None :
            return "not connected"
        
        try :
            return self.ftp.size(file_name)
        
        except ftplib.all_errors :
            return "access denied from the server"
        
    def download_file(self, file_name, local_path):
        if self.ftp is None:
            return "not connected"

        try:
    
            total_size = self.ftp.size(file_name)
            progress = 0

            with open(local_path, "wb") as down:

            # track chunk
                def callback(chunk):  # the function already has a parameter internally, make it here visible for us  (calcul such as len)
                    nonlocal progress  # nonlocal == use the variable outside the function
                    down.write(chunk)
                    progress += len(chunk) # counte the bytes in each chunk
                    loading_bar_animation(progress, total_size)

                self.ftp.retrbinary(f"RETR {file_name}", callback, 128 * 1024)  # callback now is reacieving data/chunk internally, look at my fc v1

                print()  # move to next line after bar finishes
                return "file downloaded successfully"

        except OSError:
            return "local file cannot be created (permission denied, invalid path, or disk error)"

        except ftplib.all_errors:
            return "download failed, the server rejected the request or file does not exist"



    def upload_file(self, local_path, remote_path):
        if self.ftp is None:
            return "not connected"

        if not os.path.exists(local_path):
           return "local file does not exist"

        file_name = os.path.basename(local_path)
        total_size = os.path.getsize(local_path)
        progress = 0

        try:
            with open(local_path, "rb") as up:
                def callback(chunk):
                    nonlocal progress
                    progress += len(chunk)
                    loading_bar_animation(progress, total_size)

            # pass the open file object as the second argument and the callback by name
                self.ftp.storbinary(f"STOR {remote_path}", up, 128 * 1024, callback=callback)  # upload, download have different argument orders and different callback roles

                print()  
                return f"file {file_name} uploaded successfully"

        except OSError:
            return "local file cannot be opened (not found, permission denied, or other OS error)"

        except ftplib.all_errors as e:
            return f"upload failed: {e}"
