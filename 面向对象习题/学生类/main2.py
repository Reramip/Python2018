import student

def main():
    listOfStudents = obtainListOfStudents()
    displayResults(listOfStudents)

def obtainListOfStudents():
    listOfStudents = []
    carryOn = 'Y'
    while carryOn == 'Y':
        name = input("Enter student's name: ")
        midterm = float(input("Enter student's grade on midterm exam: "))
        final = float(input("Enter student's grade on final exam: "))
        category = input("Enter category (LG or PF): ")
        if category == "LG":
            st = student.LGstudent(name, midterm, final)
        else:
            st = student.PFstudent(name, midterm, final)
        listOfStudents.append(st)
        carryOn = input("Do you want to continue (Y/N)? ")
        carryOn = carryOn.upper()
    return listOfStudents
def displayResults(listOfStudents):
    print("\nNAME\tGRADE")
    numberOfLGstudents = 0
    listOfStudents.sort(key=lambda x: x.getName())
    for pupil in listOfStudents:
        print(pupil)
        if isinstance(pupil, student.LGstudent):
            numberOfLGstudents += 1
    print("Number of letter-grade students:", numberOfLGstudents)
    print("Number of pass-fail students:", len(listOfStudents) - numberOfLGstudents)

main()
