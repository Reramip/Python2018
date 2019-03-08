class Quizzes:
    def __init__(self, gradeList=[]):
        self._gradeList = gradeList

    def average(self):
        self._gradeList.remove(min(self._gradeList))
        ave = sum(self._gradeList) / 5
        return ave

    def __str__(self):
        return str(self._gradeList)

def main():
    gradeList = []
    for i in range(6):
        gradeList.append(eval(input("Enter grade on quiz" + "{0}: ".format(i+1))))
    quiz = Quizzes(gradeList)
    print(quiz.average())
    print(quiz)

main()