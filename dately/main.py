import datetime

class Pydator:
    def __init__(self, date: datetime.date, time: datetime.time, /):
        self.date = date
        self.time = time
        self.timezone = "+00:00"

    def __str__(self):
        return f"{self.date} {self.time} {self.timezone}"

    def __repr__(self):
        return f"Pydator({self.date}, {self.time})"
