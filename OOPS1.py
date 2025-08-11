class Employee:
    def __init__(self):
        self.name = "John Doe"
        self.age = 30
        self.salary = 50000
       

    def travel(self  , destination):
            print(f"Travelling to a new destination  {destination}")

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")


# Create object and print
sam = Employee()
print(sam.salary)           # Access attribute
sam.display_details()       # Call method
sam.travel("Paris")        # Call method with argument
