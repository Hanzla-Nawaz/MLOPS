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
            self.create_account()
        elif user_input == "2":
            self.login()
        elif user_input == "3":
            print("Exiting ChatBook. Goodbye!")
            exit()




    def create_account(self):
        self.username = input("Enter your username:")
        self.password = input("Enter your password:")
        self.email = input("Enter your email: ")
        print(f"Account created successfully for {self.username}!")
        self.menu()


    def login(self):
        username = input("Enter your username:")
        password = input("Enter your password:")
        if username == self.username and password == self.password:
            print(f"Welcome back, {self.username}!")
        else:print("Invalid username or password. Please try again. ")
        self.menu()



obj = chatbook()  