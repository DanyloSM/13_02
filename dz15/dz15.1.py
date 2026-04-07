class GroupOverflowError(Exception):
    pass

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'Name:{self.first_name} surname:{self.last_name} age:{self.age} gender:{self.gender}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Name:{self.first_name} surname:{self.last_name} age:{self.age} gender:{self.gender} record_book:{self.record_book}'

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupOverflowError("Group is full")

        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None
    def __str__(self):
        if not self.group:
            return f"Number:{self.number}\nGroup is empty"
        all_students = ''
        for student in self.group:
            all_students += str(student) + "\n"
        return f"Number:{self.number}\n{all_students}"



gr = Group('PD1')

for i in range(10):
    student = Student('Male', 20 + i, f'Name{i}', f'Last{i}', f'RB{i}')
    gr.add_student(student)
try:
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    gr.add_student(st1)
except GroupOverflowError as e:
    print(e)