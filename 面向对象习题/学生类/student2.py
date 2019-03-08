class Student:
    def __init__(self, name="", midterm=0, final=0, fullTime=True):
        self._name = name
        self._midterm = midterm
        self._final = final
        self._fullTime = fullTime

    def setName(self, name):
        self._name = name

    def setMidterm(self, midterm):
        self._midterm = midterm

    def setFinal(self, final):
        self._final = final

    def getName(self):
        return self._name

class LGstudent(Student):
    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2)
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def __str__(self):
        return (self._name + '\t' + self.calcSemGrade() + '\t' +"Full-time student")

class PFstudent(Student):
    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2)
        if average >= 60:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        if self._fullTime:
            status = "Full-time student"
        else:
            status = "Part-time student"
        return (self._name + '\t' + self.calcSemGrade() + '\t' +status)