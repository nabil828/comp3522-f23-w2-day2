class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person): # Employee inherits from Person
    # Employee is a person
    def __init__(self, name, id_number):
        self.id_number = id_number
        self.name = name
        

class Student(Person):
    def __init__(self, name, student_id):
        self.student_id = student_id
        self.name = name

def main():
    p = Person("John")
    e = Employee("John", 1234)
    x = Student("Joe", 1234)

    print(p.name)
    print(e.name)
    print(x.name)
    print(e.id_number)

main()