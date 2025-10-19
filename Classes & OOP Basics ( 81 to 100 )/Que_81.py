class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade




student_no_1 = Student("Alice", 20, "A")
student_no_2 = Student("Bob", 22, "B")
student_no_3 = Student("Charlie", 21, "C")
print(f"Student 1: Name={student_no_1.name}, Age={student_no_1.age}, Grade={student_no_1.grade}")
print(f"Student 2: Name={student_no_2.name}, Age={student_no_2.age}, Grade={student_no_2.grade}")
print(f"Student 3: Name={student_no_3.name}, Age={student_no_3.age}, Grade={student_no_3.grade}")

    