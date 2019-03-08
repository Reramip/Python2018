import employee

def main():
    listOfEmployee = []
    condition = 'Y'
    numberOfEmployees = 0
    numberOfSalaried = 0
    payroll = 0
    sumHours = 0
    while condition == 'Y':
        name = input("Enter employee's name: ")
        catagory = input("Enter employee's classification (Salaried or Hourly): ").title()
        hours = eval(input("Enter the number of hours worked: "))
        if catagory == "Salaried":
            pay = eval(input("Enter weekly salary: "))
            listOfEmployee.append(employee.SalariedEmployee(name, hours, pay))
            numberOfSalaried += 1
        else:
            pay = eval(input("Enter hourly wage: "))
            listOfEmployee.append(employee.HourlyEmployee(name, hours, pay))
        numberOfEmployees += 1
        condition = input("Do you want to continue (Y/N)? ")
    print()
    for person in listOfEmployee:
        print(person)
        payroll += person.calculatePay()
        sumHours += person.getHours()
    print("Number of employees:", numberOfEmployees)
    print("Number of salaried employees:", numberOfSalaried)
    print("Total payroll: ${0:,.2f}".format(payroll))
    print("Average number of hours worked per employee: {0:.2f}".format(sumHours / numberOfEmployees))

main()