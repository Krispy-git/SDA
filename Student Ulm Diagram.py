class Person:

    def __init__(self, name, age, gender, nationality):
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality
        print(f"{self.name} was born")

    def speak(self):
        return f"Hi, my name is {self.name}. My "
    