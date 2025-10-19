class Student:


    @staticmethod
    def average(*args):
        for marks in args:
            total = sum(marks)
            avg = total / len(marks)
            print(f"Average marks: {avg}")

Student.average([85, 90, 78], [88, 92, 80], [90, 85, 87])