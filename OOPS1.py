class Employee:
    __user_id = 1
    def __init__(self):
        # print(id(self))
        self.id = Employee.__user_id
        Employee.__user_id += 1
        self.__name = "John Doe"
        self.age = 30
        self.salary = 50000
       

    def travel(self  , destination):
            print(f"Travelling to a new destination  {destination}")

    def display_details(self):
        print(f" Age: {self.age}, Salary: {self.salary}")

    @staticmethod
    def get_id():
        return Employee.__user_id
    @staticmethod
    def set_id( id):
        Employee.__user_id = id

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

        

# Create object and print
sam = Employee()
print(sam.id)  # Access id attribute
Employee.set_id(100)  # Set new user ID

ram = Employee()
print(ram.id)  # Access id attribute

mam = Employee()
print(mam.id)  # Access id attribute

print(id(sam))
sam.set_name("AHSAN ALI KHAN")  # Set new name
print(sam.get_name())
  # Get name using getter method

# sam.name = "AHSAN ALI KHAN"

# Ahsan = Employee()
# print(id(Ahsan))

# print(Ahsan.name)     # Access attribute
sam.display_details()       # Call method
sam.travel("Paris") 
print(id(sam))
       # Call method with argument
