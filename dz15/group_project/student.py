from human import Human
class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.__str__() == other.__str__()
        return NotImplemented

    def __str__(self):
        return f'Name:{self.first_name} surname:{self.last_name} age:{self.age} gender:{self.gender} record_book:{self.record_book}'