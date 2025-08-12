# class animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# class dog(animal):
#         def speak(self):
#             print(f"{self.name} barks.")    



# Animal = animal("Generic Animal")
# Animal.speak()  # Output: Generic Animal makes a sound.

# Dog = dog("Buddy")
# Dog.speak()  # Output: Buddy barks.


# SUPER KEYWORD

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, breed):
        super().__init__(breed)  # Call the parent class constructor
        self.breed = breed

    def speak(self):
        super().speak()  # Call the parent class method
        print(f"{self.name} barks and he is a {self.breed}.")

Animal = Animal("Generic Animal")
Animal.speak()  # Output: Generic Animal makes a sound.

Dog = Dog("kala Kutta")
Dog.speak()  # Output: Buddy makes a sound. Buddy barks.



