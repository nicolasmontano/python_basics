from dataclasses import dataclass, field
import datetime as dt


@dataclass
class Person():
    _name: str
    surname: str
    year_born: int
    month_born: int
    day_int: int
    dob: dt.date = field(init=False)
    money: float = field(default=0)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("new name must be 'str'")
        self._name = value

    def __post_init__(self):
        self.dob = dt.date(self.year_born, self.month_born, self.day_int)

    def add_money(self, money: float):
        self.money += money


@dataclass
class Employee(Person):
    n_employees: int = 0
    bonus_reference: float = 0

    # def __init__(self,name,surname, year_born,month_born ,day):
    #     super().__init__(name,surname, year_born,month_born ,day)
    #     salary: float = 100
    #     bonus: float = 10
    #     Employee.n_employees += 1

    # def __post_init__(self):
    #     super().__post_init__()

    @classmethod
    def change_bonus_reference(cls):
        cls.bonus_reference = 10


@dataclass
class Manager(Person):
    employees_in_charge: list = field(default_factory=list)


a = Employee("nico", "montano", 1992, 1, 1)
print(a)
