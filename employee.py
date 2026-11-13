class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary / 52

class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def calculate_paycheck(self, weekly_hours):
        return self.hourly_rate * weekly_hours

class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales_number, commission_rate):
        super().__init__(fname, lname, salary)
        self.sales = sales_number
        self.commission_rate = commission_rate

    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck()
        total_commission = self.sales * self.commission_rate

        return regular_salary + total_commission

