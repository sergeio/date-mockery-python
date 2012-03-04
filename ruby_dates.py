from datetime import datetime, timedelta

class DateNumber(object):

    def __getitem__(self, attr):
        return Number(attr)


class Number(object):

    def __init__(self, number):
        self.number = number

    def __getattr__(self, attr):
        return Direction(self.number, attr)


class Direction(object):

    def __init__(self, number, units):
        self.number = number
        self.units = units

    @property
    def ago(self):
        return self.delta(-1)

    @property
    def ahead(self):
        return self.delta(1)

    def delta(self, direction):
        return datetime.utcnow() + timedelta(
            **{self.units: direction * self.number})
