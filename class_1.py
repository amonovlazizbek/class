class Student:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.bosqich = 1

    def get_name(self):
        return self.name

    def get_lastname(self):
        return self.lastname

    def get_age(self):
        return self.age

    def get_bosqich(self):
        return self.bosqich

    def get_info(self):
        return f"{self.name} {self.lastname}, {self.age} years old"

    def introduce(self):
        return f"Hello, my name is {self.name} {self.lastname} and I am {self.age} years old."


student1 = Student("Alice", "Smith", 20)
print(student1.introduce())

student2 = Student("John", "Johnson", 22)
print(student2.introduce())

print(student1.get_age())
