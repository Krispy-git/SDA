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
    
    def __init__(self, name, age, gender, nationality, school, grade, subjects_studied, credits):
        super().__init__(name, age, gender, nationality)
        self.school = school
        self.grade = grade
        self.subjects_studied = subjects_studied
        self.credits = credits
        print(f"{self.name} studies at {self.school} in the {self.grade} grade.")

    def study(self):
        print(f"{self.name} is very busy at {self.school}")
        return f"{self.name} is busy not getting bitches."
            
    def complain(self):
        return f"{self.name} is complaining about {self.school}"

#    def passExam(self, credits)

    def failExam(self):
        return f"{self.name} failed his exam."

john = Person("John", '20', "male", "Jamaican")
john.speak()
john.eat()
billy = Student("Billy", '19', "female", "dutch","Fontys", '2', "mechanical", '110')
billy.study()