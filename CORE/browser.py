def dir_browsing(ftp):

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

