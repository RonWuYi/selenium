class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        return "{0}-{1}-{2}".format(self.month, self.day, self.year)

    @staticmethod
    def millenium(month, day):
        return Date(month, day, 3999)
    # @classmethod
    # def from_string(cls, date_as_string):
    #     day, month, year = map(int, date_as_string.split('-'))
    #     date1 = cls(day, month, year)
    #     return date1
    #
    # @staticmethod
    # def is_date_valid(date_as_string):
    #     day, month, year = map(int, date_as_string.split('-'))
    #     return day <= 31 and month <= 12 and year <= 3999


new_year = Date(1, 1, 2013)
millenium_new_year = Date.millenium(2, 2)

print(new_year.display())
print(millenium_new_year.display())

print(isinstance(new_year, Date))