from CORE.clients import FTPClient
from CORE.browsing import dir_browsing_file, dir_browsing_folder, selected_file
import os
from CORE.helper import folder_scanner

def main():
    host = input("Enter FTP host: ").strip()
    port = int(input("Enter FTP port: ").strip())
    username = input("Enter username (leave empty for anonymous): ").strip()
    password = input("Enter password (leave empty for anonymous): ").strip()

    ftp = FTPClient(host, port, username, password)
    ftp.connect()
    ftp.login()

    print("\nConnected successfully.\n")

    while True:
        print("\n=== FTP MAIN MENU ===")
        print("1. Browse server")
        print("2. Download file")
        print("3. Upload file")
        print("4. Delete file")
        print("5. Rename file")
        print("6. Change directory")
        print("7. Show current path")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        # EXIT
        if choice == "0":
            print("Goodbye.")
            break

        # BROWSE
        elif choice == "1":
            selected = dir_browsing_file(ftp)
            if selected:
                print(f"Selected file: {selected}")

        # DOWNLOAD
        elif choice == "2":
            print("\nSelect a file to download:")
            file_name = dir_browsing_file(ftp)
            if file_name:
                local_path = os.path.join("downloads", file_name)
                os.makedirs("downloads", exist_ok=True)
                print(ftp.download_file(file_name, local_path))

        # UPLOAD (new version)
        elif choice == "3":
           local_path = input("Enter local file path to upload: ").strip()
           if not os.path.exists(local_path):
               print("Local file does not exist.")
               continue
           files = folder_scanner(local_path)
           path = selected_file(files)
           path_remote = dir_browsing_folder(ftp)
           file_name = os.path.basename(path)
           new_path = os.path.join(path_remote, file_name)  # in oredre to upload we need the full path included with the file name sent by the user
        

           print(ftp.upload_file(path, new_path))

        # DELETE
        elif choice == "4":
            print("\nSelect a file to delete:")
            file_name = dir_browsing(ftp)
            if file_name:
                print(ftp.delete_file(file_name))

        # RENAME
        elif choice == "5":
            print("\nSelect a file to rename:")
            file_name = dir_browsing(ftp)
            if file_name:
                print(ftp.rename_file(file_name))

        # CHANGE DIRECTORY
        elif choice == "6":
            path = input("Enter directory path: ").strip()
            print(ftp.change_directory(path))

        # CURRENT PATH
        elif choice == "7":
            print("Current path:", ftp.current_path())

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
