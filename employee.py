"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
# import enum as Enum
#
# CommissionType = Enum('CommissionType', 'none bonus cpc')
# EmployeeType = Enum('EmployeeType', 'salary hourly')



class Comission:
    def __init__(self, wage=0):
        self.wage = wage

    def bonusString(self):
        return ""

class BonusComission(Comission):
    def __init__(self, bonus):
        super().__init__(bonus)
        self.bonus = bonus

    def bonusString(self):
        return f" and receives a bonus commission of {self.bonus}"

class PerContractComission(Comission):
    def __init__(self, contracts, cpc):
        super().__init__(contracts * cpc)
        self.contracts = contracts
        self.cpc = cpc

    def bonusString(self):
        return f" and receives a commission for {contracts} contract(s) at {cpc}/contract"


class Salary:
    def __init__(self, total=0, comission=Comission()):
        self.total = total
        self.comission = comission

class HourlySalary(Salary):
    def __init__(self, hours, perhour, comission=Comission()):
        super().__init__(total=((hours*perhour)+comission.wage), comission=comission)
        self.hours = hours
        self.perhour = perhour

    def salaryString(self):
        return f"Jan works on a contract of {self.hours} hours at {self.perhour}/hour" + self.comission.bonusString + f". Their total pay is {self.total}."

class MonthlySalary(Salary):
    def __init__(self, monthly, comission=Comission()):
        super().__init__(total=(monthly+comission.wage), comission=comission)
        self.monthly = monthly

    def salaryString(self):
        return f"Billie works on a monthly salary of {self.monthly}" + self.comission.bonusString + f". Their total pay is {self.total}."




class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_pay(self):
        return self.salary.total
        # total = 0
        # if self.employeetype == EmployeeType.salary:
        #     total += wage*months
        # elif self.employeetype == EmployeeType.hourly:
        #     total += wage*hours
        # else:
        #     pass
        #
        # if self.comissiontype == CommissionType.none:
        #     pass
        # elif self.comissiontype == CommissionType.bonus:
        #     total += self.bonus
        # elif self.comissiontype == CommissionType.cpc:
        #     total += self.contracts*self.commissionpercontract
        # else:
        #     pass
    def __str__(self):
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlySalary(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlySalary(100, 25))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlySalary(3000, PerContractComission(4, 200)))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlySalary(100, 25, PerContractComission(3, 220)))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlySalary(2000, BonusComission(1500)))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlySalary(120, 30, BonusComission(600)))
