from CORE.clients import FTPClient
from CORE.browsing import dir_browsing_file, dir_browsing_folder, selected_file
import os
from CORE.helper import folder_scanner, check_id

def main():
        
    host = check_id()
    port = int(input("Enter FTP port: ").strip())
    username = input("Enter username (leave empty for anonymous): ").strip()
    password = input("Enter password (leave empty for anonymous): ").strip()


    ftp = FTPClient(host, port, username, password)
    ftp.connect()
    ftp.login()

    print("\nConnected successfully.\n")
    print(f"host : {host}, port : {port}")

    while True:
        print("\n=== FTP MAIN MENU ===")
        print("1. Browse server")
        print("2. Download file")
        print("3. Upload file")
        print("4. Delete file")
        print("5. Rename file")
        print("6. Show current path")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

    
        if choice == "0":
            ftp.close()
            print("Goodbye, your are disconnected")
            ftp.close()
            break

        elif choice == "1":
            selected = dir_browsing_file(ftp)
            if selected:
                print(f"Selected file: {selected}")

    
        elif choice == "2":
            print("\nSelect a file to download:")
            file_name = dir_browsing_file(ftp)
            if file_name:
                local_path = os.path.join("downloads", file_name)
                os.makedirs("downloads", exist_ok=True)
                print(ftp.download_file(file_name, local_path))

        
        elif choice == "3":
            local_path = input("Enter local folder path that you want to scan (return files within it): ").strip()
            if not os.path.exists(local_path):
                print("Local file does not exist.")
                continue
           
            files_paths = folder_scanner(local_path)
            file_path = selected_file(files_paths)
            path_remote = dir_browsing_folder(ftp)
            file_name = os.path.basename(file_path)
            new_path = os.path.join(path_remote, file_name)  # in oredre to upload we need the full path included with the file name sent by the user
        

            print(ftp.upload_file(file_path, new_path))
            

        elif choice == "4":
            print("\nSelect a file to delete:")
            file_name = dir_browsing_file(ftp)
            if file_name:
                print(ftp.delete_file(file_name))

    
        elif choice == "5":
            print("\nSelect a file to rename:")
            file_name = dir_browsing_file(ftp)
            path = ftp.current_path()
            file_path = os.path.join(path,file_name)
            if file_path:
                print(ftp.rename_file(file_path))


        elif choice == "6":
            print("Current path:", ftp.current_path())

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
