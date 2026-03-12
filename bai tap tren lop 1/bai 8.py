class Student:
    def __init__(self,Ten, Diem):
        if Diem < 0 or Diem > 10:
            raise ValueError('Diem nay khong nam trong khoang 0-10')
        self.Ten = Ten
        self.Diem = Diem
sv1 = Student('cong minh', 10)
sv2 = Student('hieu minh', 9.5)