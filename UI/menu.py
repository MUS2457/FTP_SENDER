class Menu :

    def start(self) :
        while True :
            self.show_menu()

            if not self.validator() :
                break

    def show_menu(self) :
        print("=== FTP SENDER by RaijinCode ⚡️ ===")
        print("1. upload file")
        print("2. download file")
        print("3. close")

    def validator(self) :
        number = [1,2,3]

        user = input(f"Enter your choice based on number from {number}: ").strip()

        if not user.isdigit() or int(user) not in number :
            print("Invalid input")
            return True   
        
        user = int(user)

        
        if user == 1 :
            self.upload_file()
        elif user == 2 :
            self.download_file()
        elif user == 3 :
            print("Goodbye!")
            return False   
    
        return True   
    
    def upload_file(self) :
        pass
    
    def download_file(self) :   
        pass
