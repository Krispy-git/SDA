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
    def drink(self):
        print(f"now I am not thirsty!")
        return f"{self.name} drinks"    
    
class Student(Person):
    
    def __init__(self, school, grade, subjects_studied, credits):
        super().__init__()
        self.school = school
        self.grade = grade
        self.subjects_studied = subjects_studied
        self.credits = credits
        print(f"{self.__Person__.__name__} studies at {self.school} in the {self.grade} grade.")

    def study(self):
        return f"{self.__Person__.__name__} is busy not getting bitches."
    
    def complain(self):
        return f"{self.__Person__.__name__} is complaining about {self.school}"

#    def passExam(self, credits)

    def failExam(self):
        return f"{self.__Person__.__name__} failed his exam."

    
