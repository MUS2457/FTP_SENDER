from CORE.clients import FTPClient

def main():
    # PS4 GoldHEN FTP server info
    host = "192.168.40.154"
    port = 2221             
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

    # Upload test
    print("\nUploading test.txt...")
    print(ftp.upload_file("test.txt"))

    # Download test
    print("\nDownloading test.txt...")
    print(ftp.dowload_file("test.elf"))

    print("\nDone.")


if __name__ == "__main__":
    main()
