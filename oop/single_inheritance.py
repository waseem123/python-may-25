class Person:
    name = "<NAME>"
    age = 0

    def set_person(self, name, age):
        self.name = name
        self.age = age

    def get_person(self):
        print(f'Name - {self.name}')
        print(f'Age  - {self.age}')

class Student(Person):
    roll_no = 0
    std = 0
    div = ''

    def set_student(self, roll_no, std, div):
        self.roll_no = roll_no
        self.std = std
        self.div = div

    def get_student(self):
        print(f'Roll No - {self.roll_no}')
        print(f'Std - {self.std}')
        print(f'Division - {self.div}')


# p = Person()
# p.set_person('Usaid', 10)
# p.get_person()

s = Student()
s.set_person("Shravani",10)
s.set_student(108, 5,'A')

s.get_person()
s.get_student()
