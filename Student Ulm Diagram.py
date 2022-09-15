class Person:

    def __init__(self, name, age, gender, nationality):
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality
        print(f"{self.name} was born")

    def speak(self):
        print(f"woof")
        return f"Hi, my name is {self.name}. I am {self.age} years old."

    def sleep(self):
        print(f"zzzz")
        return f"{self.name} is sleeping"
    def eat(self):
        print(f"nom nom nom so tasty")
        return f"{self.name} has eaten"
    def drink(self:)
        print(f"now I am not thirsty!")
        return f"{self.name} drinks"    
    