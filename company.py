from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

def main():
    my_company = Company()
    emp1 = SalaryEmployee('John', 'Doe', 52000)
    emp2 = HourlyEmployee('Jane', 'Smith', 40, 30)
    emp3 = CommissionEmployee('Alice', 'Johnson', 78000, 50, 0.1)
    my_company.add_employee(emp1)
    my_company.add_employee(emp2)
    my_company.add_employee(emp3)
    for emp in my_company.employees:
        if isinstance(emp, SalaryEmployee):
            print(f"{emp.fname} {emp.lname} earns {emp.salary} annually and ${emp.calculate_paycheck():,.2f} weekly.")
        elif isinstance(emp, HourlyEmployee):
            print(f"{emp.fname} {emp.lname} earns ${emp.hourly_rate} per hour and ${emp.calculate_paycheck(emp.weekly_hours):,.2f} weekly.")
        elif isinstance(emp, CommissionEmployee):
            print(f"{emp.fname} {emp.lname} earns ${emp.salary} annually and ${emp.calculate_paycheck():,.2f} weekly.")
    print('-----------------')

main()