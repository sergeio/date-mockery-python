from datetime import datetime, timedelta


class DateNumber(object):

    def __init__(self, date):
        self.now = date

    def __getitem__(self, attr):
        return DateUnits(self.now, attr)

    __call__ = __getitem__


class DateUnits(object):

    def __init__(self, date, number):
        self.date = date
        self.number = number

    def __getattr__(self, attr):
        return DateDirection(self.date, self.number, attr)


class DateDirection(object):

    def __init__(self, date, number, units):
        self.date = date
        self.number = number
        self.units = units

    @property
    def ago(self):
        return self.delta(-1)

    @property
    def ahead(self):
        return self.delta(1)

    def delta(self, direction):
        return self.date + timedelta(**{self.units: direction * self.number})
