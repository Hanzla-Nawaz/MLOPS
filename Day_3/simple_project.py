class chatbook():
    def __init__(self):
        self.username = ""
        self.password = ""
        self.email = ""
        self.menu()

    def menu(self):
        user_input = input("""Welcome to ChatBook!
Please choose an option:
1. Create Account
2. Login    
3. Exit
Enter your choice: """)
        if user_input == "1":
                pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Exiting ChatBook. Goodbye!")
            exit()

