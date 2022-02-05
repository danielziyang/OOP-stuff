class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay 
        

        Employee.num_of_emps += 1

    @property 
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @fullname.setter 
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first 
        self.last = last

    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amount)

    def __repr__(self):
        return f'Employee({self.first}, {self.last}, {self.pay})' 


    @classmethod 
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod 
    def from_string(cls, emp_str): 
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod 
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False 
        return True  

emp_1 = Employee('Corey', 'Schafer', 50000) 
#emp_2 = Employee() 

print(emp_1)
#print(emp_2) 

Employee.raise_amount = 1.05 #changes the class variable for all instances

emp_1.raise_amount = 1.06 #changes only to a specific instance


print(emp_1.fullname)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang 

     

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
print(dev_1.prog_lang)

print(isinstance(dev_1, Developer))
print(issubclass(Developer, Employee))