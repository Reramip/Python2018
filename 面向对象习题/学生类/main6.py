import student2

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
            st = student2.LGstudent(name, midterm, final)
        else:
            fullTime = input("Are you a full-time student (Y/N)? ")
            if fullTime == 'Y':
                st = student2.PFstudent(name, midterm, final, True)
            else:
                st = student2.PFstudent(name, midterm, final, False)
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

main()
