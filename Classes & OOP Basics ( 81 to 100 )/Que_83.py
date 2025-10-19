class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_info(self):
        print(f"Name={self.name}")
        print(f"Age={self.age}") 
        print(f"Grade={self.grade}")

student_no_1 = Student("Alice", 20, "A")
student_no_2 = Student("Bob", 22, "B")
student_no_3 = Student("Charlie", 21, "C")
student_no_1.get_info()
