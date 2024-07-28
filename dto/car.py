import time
from dataclasses import dataclass, field
import datetime as dt

@dataclass
class car():
    plate: str
    date_production :dt.date =dt.datetime.now(tz=dt.timezone.utc)
    owners: list[int] = field(default_factory=list)


    def calc_days_since_created(self):
        return (dt.datetime.now(tz=dt.timezone.utc)-self.date_production).days


if __name__ == '__main__':
    car_1=car("ax123")
    time.sleep(10)
    print(car_1.calc_days_since_created())


