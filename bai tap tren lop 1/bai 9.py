class Student:
    def __init__(self,Ten, Diem):
        self.Ten = Ten
        self.Diem = Diem
    def display(self):
        print(f"Sinh vien {self.Ten} co diem la {self.Diem}")
sv1 = Student('nguyen duy viet', 10)
sv2 = Student('ha gia bao', 9.5)
sv1.display()
sv2.display()