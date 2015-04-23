conf = {
'exam_max': 30,
'lab_max': 7,
'lab_num': 10,
'k': 0.61
}

class Student:
    name = None
    con = None
    lab = None
    exam = None
    def __init__(self, name, conf):
        self.name = str(name)
        self.con = conf
        self.lab = [c * 0 for c in range(self.con.get("lab_num"))]

    def make_exam(self, m):
        if m > self.con.get("exam_max"):
            self.exam = self.con.get("exam_max")
        else:
            self.exam = m
        return self

    def make_lab(self, m, n = -1):
        if m > self.con.get('lab_max'):
            m = self.con.get('lab_max')
        if n == -1:
            for i in range(0, len(self.lab)):
                if self.lab[i] == 0:
                    self.lab[i] = m
                    break
        elif n > self.con.get('lab_num') - 1:
            return self
        else:
            self.lab[n] = m
        return self

    def is_certified(self):
        s = 0
        for i in self.lab:
            s += i
        if self.exam == None:
            self.exam = 0
        s += self.exam
        if s >= self.con.get("k") * 100:
            return s, True
        else:
            return s, False

oleg = Student('Oleg', conf)
oleg.make_lab(40).make_lab(7,5).make_lab(1).make_lab(7).make_lab(7).make_lab(7).make_lab(7,1).make_lab(7).make_exam(7)
print oleg.is_certified()

