class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}."

# Create an instance of the Person class
person1 = Person("Grace", 19, "female")

# Call the introduce method to display the person's information
print(person1.introduce())

