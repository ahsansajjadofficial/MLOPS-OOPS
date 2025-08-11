class facebook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.logged_in = False
        self.menu()

    def menu(self):
        input_username = input(""" 
                                Welcome to Facebook!
                               what like you want to do?
                                1. Sign up
                                2. Log in
                                3. Log out
                                4. Write a post
                                5. Exit
                                6. Send the message to friend
                                7. View profile""")
        if input_username == '1':
            self.sign_up()  
        elif input_username == '2':
            self.log_in()
        elif input_username == '3':
            self.log_out()
        elif input_username == '4':
            self.write_post()
        elif input_username == '5':
            print("Exiting the application. Goodbye!")
            exit()
        elif input_username == '6':
            self.send_message()
        elif input_username == '7':
            self.view_profile()
        else:
            print("Invalid option. Please try again.")
            self.menu()

    def sign_up(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        print(f"User {self.username} signed up successfully!")
        self.menu()
        self.logged_in = True

    def log_in(self):
        if not self.username or not self.password:
            print("Please sign up first.")
            self.menu()
        else:
            input_username = input("Enter your username: ")
            input_password = input("Enter your password: ")
            if input_username == self.username and input_password == self.password:
                print(f"User {self.username} logged in successfully!")
                self.logged_in = True
                self.menu()
            else:
                print("Invalid credentials. Please try again.")
                self.menu()

    def log_out(self):
        if self.logged_in:
            print(f"User {self.username} logged out successfully!")
            self.logged_in = False
        else:
            print("You are not logged in.")
        self.menu()

    def write_post(self):
        if self.logged_in:
            post_content = input("Write your post: ")
            print(f"Post created: {post_content}")
        else:
            print("You need to log in to write a post.")
        self.menu()


    def send_message(self):
        if self.logged_in:
            friend_username = input("Enter the username of your friend: ")
            message = input("Enter your message: ")
            print(f"Message sent to {friend_username}: {message}")
        else:
            print("You need to log in to send a message.")
        self.menu()

    def view_profile(self):
        if self.logged_in:
            print(f"Profile of {self.username}:")
            print(f"Username: {self.username}")
            print("Posts: None")
        else:
            print("You need to log in to view your profile.")

   
object = facebook()