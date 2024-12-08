
class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):

        marital_status = "married" if self.is_married else "not married"
        print(f"My name is {self.full_name},  I am {self.age}, I am {marital_status}")
class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average_marks(self):
        if self.marks:
            average_marks = sum(self.marks.values())/len(self.marks)
            return round(average_marks, 2)
        else:
            return 0
class Teacher(Person):
    base_salary = 500

    def __init__(self, full_name, age, is_married, experience, base_salary):
        super().__init__(full_name, age, is_married)
        self.experience = experience


    def total_salary(self):
        if self.experience > 3:
            years_above_three = self.experience - 3
            bonus = years_above_three * 0.05 * self.base_salary
        else:
            bonus = 0
        return self.base_salary + bonus

teacher = Teacher("Jane Eyre", 30, True, 12, 500)
teacher.introduce_myself()
print(f'Salary: {teacher.total_salary()}')

def create_students():
    students = [
        Student("Tomas Jones", 16, False, {"Math": 4, "History": 5, "Biology": 3}),
        Student("Ann Miller", 17, False, {"Math": 5, "History": 4, "Biology": 5}),
        Student("David Wood", 18, False, {"Math": 3, "History": 4, "Biology": 4})
    ]
    return students

students = create_students()

for student in students:
    student.introduce_myself()
    print(f'Marks: {student.marks}')
    print(f"Average mark: {student.average_marks()}")

