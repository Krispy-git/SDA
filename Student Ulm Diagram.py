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
        credits= int
        print(f"{self.name} studies at {self.school} in the {self.grade} grade.")

    def study(self):
        print(f"{self.name} is very busy at {self.school}")
        return f"{self.name} is busy not getting bitches."
            
    def complain(self):
        return f"{self.name} is complaining about {self.school}"

    def passExam(self):
        print(f"{self.name} has passed his {self.subjects_studied} exam and has earned 4 more credits!")
    


    def failExam(self):
        return f"{self.name} failed his exam."

#just testing how to commit

class Teacher(Person):
    def __init__(self, name, age, gender, nationality, school, subjects_taught,hours_worked,classes_taought):
        super().__init__(name, age, gender, nationality)
        self.school = school
        self.subjects_taught = subjects_taught
        self.hours_worked = hours_worked
        self.classes_taught = classes_taought
        print("A teacher is now employed")

    def teach(self):
        print(f"{self.name} is now giving a lecture about {self.subjects_taught}!") 

    def makeExam(self):
        print(f"{self.name} is now making a very hard {self.subjects_taught} exam to give to his {self.classes_taught}.")
        return f"He already knows that 75% will fail"    

    def shout(self): 
        print("@#!*& @& #*&@!")      
        return f"{self.name} is angry"     
             

john = Person("John", '20', "male", "Jamaican")
john.speak()
john.eat()
billy = Student("Billy", '19', "female", "dutch","Fontys", '2', "mechanical", '110')
billy.study()
gosho=Teacher('Gosho','42', 'male','Serbian','fontys','programming','16hours a week','2 international classes')
print(gosho.speak())
gosho.shout()
billy.passExam()