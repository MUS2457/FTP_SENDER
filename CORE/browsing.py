import os

def dir_browsing_file(ftp):

    while True:
        all_items = list(ftp.info_items())
        print("Current path:", ftp.current_path())
        print("Items:", [item["name"] for item in all_items])

        for i, item in enumerate(all_items, start=1):
            icon = "[DIR]" if item["type"] == "dir" else "[FILE]"
            print(f"{i}. {icon} {item['name']}")

        user = input("Enter number (or 0 for Back), 'exit' to quit: ").strip()

        if user == "exit":
            print("Return to main menu")
            return 
        
        elif user == "0":
            ftp.change_directory("..")   # .. back to parent directory
            continue

        elif not user.isdigit():
            print("Invalid input")
            continue

        index = int(user) - 1    # indexing instead of my old way of (dic enumerated)

        if index < 0 or index >= len(all_items):  
            print("Invalid input")
            continue

        choice = all_items[index]

        if choice["type"] == "file":
            return choice["name"]

        ftp.change_directory(choice["name"])



def dir_browsing_folder(ftp):

    while True:
        all_items = list(ftp.info_items())
        print("Current path:", ftp.current_path())
        print("Folders:")

        dirs = [item for item in all_items if item["type"] == "dir"]  # only folders

        for i, item in enumerate(dirs, start=1):
            print(f"{i}. [DIR] {item['name']}")

        print("0. Back")
        print("select. Choose this folder")

        user = input("Enter choice: ").strip()

        if user.lower() == "select":
            return ftp.current_path()

        
        elif user == "0":
            ftp.change_directory("..")
            continue

        elif not user.isdigit():
            print("Invalid input")
            continue

        index = int(user) - 1

        if index < 0 or index >= len(dirs):
            print("Invalid input")
            continue

        ftp.change_directory(dirs[index]["name"])



def selected_file(all_files) :
    if not all_files:
        print("This Dir path doesnt have any files")
        return 
    
    while True :
        results = {i:f for i,f in enumerate(all_files, start = 1)}

        for i, f in results.items() :
            file_name = os.path.basename(f)
            file_size = os.path.getsize(f) / 1024**2
            print(f"{i}. file {file_name} ,size {file_size} mb.")

        user = input("Enter the number of file you want to send or '0' to quit").strip()

        if user == '0' :
            print("Returning to main menu!")
            return
            
        elif not user.isdigit() :
            print("Only a number is allowed")
            continue

        index = int(user) -1
        if index < 0 or index >= len(all_files) :
            print("the number entered doesnt match any file")
            continue

        file_path = all_files[index]
        
        print(f"file that have been selected {os.path.basename(file_path)} , size {os.path.getsize(file_path)/ 1024**2} Mb.")

        return file_path






