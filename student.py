from person import Person

class Student(Person):
    def __init__(self, name):
        super().__init__(name)  # same as self.name = name
        self.courses_enrolled = []