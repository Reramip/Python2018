import lgStudent

def main():
    listOfStudents = []
    carryOn = 'Y'
    while carryOn == 'Y':
        st = lgStudent.LGstudent()
        name = input("Enter student's name: ")
        midterm = float(input("Enter student's midterm grade: "))
        final = float(input("Enter student's final grade: "))
        st=lgStudent.LGstudent(name, midterm, final)
        listOfStudents.append(st)

        carryOn = input("Continue(Y/N)? ")
        carryOn = carryOn.upper()
    print("\nNAME\tGRADE")
    for student in listOfStudents:
        print(student)

main()