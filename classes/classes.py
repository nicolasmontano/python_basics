from typing import Union, List, Type, TypeVar, Optional, Dict
import numpy as np

T = TypeVar('T', bound='Employee')

class Employee:
    """
    Class variables
    self.variale= you want to be able to be different among instances.
    Class.variable= you want to be the same for all the instances.
    """
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):

        self._first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    def __repr__(self):
        return f"Employee(first={self.first}, last={self.last}, pay= {self.pay})"

    def full_name(self):
        return '{} {}'.format(self._first, self.last)

    # the created attribute can only be set with setter method
    @property
    def first(self):
        return self._first

    @first.setter
    def change_firs(self, value: str):
        self._first = value

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # class methods are to access cls or update for all classes  state and class contructor
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

    # does not require an entity or cls e.g.Employee.calc_avg_sal([1,1,1,2])
    # Employee.calc_avg_sal([1,1,1,2])
    # employee
    @staticmethod
    def calc_avg_sal(salaries: List[Union[float, int]]) -> float:
        if not salaries:
            return 0
        else:
            return float(np.average(salaries))


class Manager(Employee):
    def __init__(self, first, last, pay, employees: Optional[Dict[str, Employee]] = None):
        if not employees:
            self.employees = dict()
        else:
            self.employees = employees

        super().__init__(first, last, pay)

    def add_employee(self, employee: Employee):
        self.employees[employee.email] = employee

    def remove_employee(self, employee: Employee):
        if employee.email in self.employees:
            self.employees.pop(employee.email)
        else:
            print(f"employee with email {employee.email} not in Manager")


em1 = Employee.create_inst_from_string("nico-montano-1")
em2 = Employee.create_inst_from_string("nico-montano-1")
em3 = Employee.create_inst_from_string("andres-torres-1")
manager_1 = Manager.create_inst_from_string("andres-montes-100")

manager_1.add_employee(em2)
manager_1.add_employee(em3)
