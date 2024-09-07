from dataclasses import dataclass, field
from typing import Union, TypeVar, List
from statistics import mean

T = TypeVar('T', bound='Employee')


@dataclass
class Employee:
    _first: str
    last: str
    pay: Union[int, float] = field(default=0)
    full_name: str = field(init=False)

    # class variables
    num_of_emps = 0
    raise_amt = 1.04


    def __post_init__(self):
        Employee.num_of_emps += 1
        self.email =  f"{self.first}.{self.last}@company.com"
        self.full_name = f"{self.first} {self.last}"

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, value: str):
        if not isinstance(value, str):
            raise TypeError(f"value must be str, got {type(value).__name__}")
        elif len(value) < 3:
            raise ValueError("Len for value to change first must be bigger than 2")
        else:
            self._first = value

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # class methods are to access cls or update for all basics  state and class contructor
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def create_inst_from_string(cls, emp_str: str) -> T:
        first, last, pay = emp_str.split('-')
        try:
            pay = float(pay)
        except ValueError:
            print("To create an employee with constructor, pay must be int or float")
        else:
            return cls(first, last, pay)

    @staticmethod
    def calc_avg_sal(salaries: List[Union[float, int]]) -> float:
        if not salaries:
            return 0
        else:
            return mean(salaries)


@dataclass
class Manager(Employee):
    employees: dict = field(default_factory=dict)

    def add_employee(self, employee: Employee):
        self.employees[employee.email] = employee

    def remove_employee(self, employee: Employee):
        if employee.email in self.employees:
            self.employees.pop(employee.email)
        else:
            print(f"Employee with email {employee.email} not found in Manager's employees")

if __name__ == '__main__':

    em1 = Employee.create_inst_from_string("nico-montano-1")
    em2 = Employee.create_inst_from_string("nico-montano-1")
    em3 = Employee.create_inst_from_string("andres-torres-1")
    manager_1 = Manager.create_inst_from_string("andres-montes-100")
    print(manager_1)
