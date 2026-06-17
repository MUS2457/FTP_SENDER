def dir_browsing(ftp):

    while True:
        all_items = list(ftp.info_items())
        print("Current path:", ftp.current_path())
        print("Items:", [item["name"] for item in all_items])

        results = {i: f for i, f in enumerate(all_items, start=1)}

        for index, item in results.items():
            print(f"{index}. {item['name']}")

        user = input("Enter the number of the file you want to download: ").strip()

        if not user.isdigit() or int(user) not in results:
            print("Invalid input, please enter a number from the list")
            continue

        choice = results[int(user)]

        # If it's a file → return it
        if choice["type"] == "file":
            return choice["name"]

        # If it's a directory → enter it
        ftp.change_directory(choice["name"])
