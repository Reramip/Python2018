import studentWithStatus

def main():
    name = input("Enter student's name: ")
    midterm = float(input("Enter student's grade on midterm exam: "))
    final = float(input("Enter student's grade on final exam: "))
    category = input("Enter category (LG or PF): ")
    if category.upper() == "LG":
        st = studentWithStatus.LGstudent(name, midterm, final)
    else:
        question = input("Is " + name + " a full-time student (Y/N)? ")
        if question.upper() == 'Y':
            fullTime = True
        else:
            fullTime = False
        st = studentWithStatus.PFstudent(name, midterm, final, fullTime)
    semesterGrade = st.calcSemGrade()
    print("\nNAME\tGRADE\tSTATUS")
    print(st)

main()