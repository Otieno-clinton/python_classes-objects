class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print("Hello, my name is " + self.name +" I am "+str(self.age)+" years old and I identify as "  +self.gender)

# Create an instance of Person and call the introduce method
person1 = Person("Otieno Clinton", 25, "Male")
person1.introduce()
