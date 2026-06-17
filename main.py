from CORE.clients import FTPClient
from CORE.browser import dir_browsing

def main():
    # PS4 GoldHEN FTP server info
    host = "192.168.40.175"
    port = 2121             
    username = ""           
    password = ""           

    ftp = FTPClient(host, port, username, password)

    # Connect
    print("Connecting...")
    try:
        ftp.connect()
        print("Connected successfully")
    except Exception as e:
        print("Connection failed:", e)
        return

    # Login
    print("Logging in...")
    result = ftp.login()
    if result is not None:
        print(result)

    # List files
    print("\nListing files:")
    print(ftp.list_files())
    print("Current path:", ftp.current_path())


    # Download test
    print("\nDownloading test.txt...")
    file = dir_browsing( ftp)
    print("Items count:", ftp.info_items())

    print(ftp.dowload_file(file))
    print("Current path:", ftp.current_path())


    print("\nDone.")


if __name__ == "__main__":
    main()
