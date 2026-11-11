from employee import Employee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

def main():
    my_company = Company()
    emp1 = Employee('John', 'Doe', 52000)
    emp2 = Employee('Jane', 'Smith', 60000)
    my_company.add_employee(emp1)
    my_company.add_employee(emp2)
    for emp in my_company.employees:
        print(f"{emp.fname} {emp.lname} earns {emp.salary} annually and ${emp.calculate_paycheck():,.2f} weekly.")
    print('-----------------')

main()