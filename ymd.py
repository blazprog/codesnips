class YMD:
    def __init__(self, years, months, days):
        self.years = years
        self.months = months
        self.days = days

    def __add__(self, other):
        month_increment = year_increment = 0
        days = self.days + other.days
        if days > 29:
            days -= 30
            month_increment = 1
        months = self.months + other.months + month_increment
        if months > 11:
            months -= 12
            year_increment = 1
        years = self.years + other.years + year_increment
        return YMD(years, months, days)

    def __sub__(self, other):
        other_month_increment = 0
        other_year_increment = 0
        days = self.days - other.days
        if days < 0:
            other_month_increment = 1
            days = self.days + (30-other.days)
        months = self.months - (other.months + other_month_increment)
        if months < 0:
            months = (12 - other.months  - other_month_increment) + self.months
            other_year_increment = 1
        years = self.years - (other.years + other_year_increment)
        return YMD(years, months, days)

    def __str__(self):
        return "{:02d}-{:02d}-{:02d}".format(self.years,
                                             self.months,
                                             self.days)

    def __lt__(self, other):
        return (self.years * 365 + self.months * 30 + self.days <
                other.years * 365 + other.months * 30 + other.days)

    def __gt__(self, other):
        return (self.years * 365 + self.months * 30 + self.days >
                other.years * 365 + other.months * 30 + other.days)

    def __eq__(self, other):
        return(
            self.years == other.years and
            self.months == other.months and
            self.days == other.days
        )


class Month:
    @classmethod
    def next_month_firs_day(cls, d):
        month = d.month + 1
        if month == 13:
            month = 1
            year = d.year + 1
        else:
            year = d.year
        return cls(year, month)

    @classmethod
    def previous_month_last_day(cls, d):
        month = d.month - 1
        if month == 0:
            month = 12
            year = d.year - 1
        else:
            year = d.year
        return cls(year, month)

    def __init__(self, year, month):
        self.year = year
        self.month = month

    def inc_month(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1

    def __str__(self):
        return "{}-{:02d}".format(self.month, self.year)

    def __eq__(self, other):
        if self.year == other.year and self.month == other.month:
            return True
        else:
            return False

    def __lt__(self, other):
        if (self.year < other.year):
            return True
        elif self.year > other.year:
            return False
        else:
            return self.month < other.month


    @staticmethod
    def count_months(_d1, _d2):
        # vrne stevilo mesecev  med d1 in d2, vkljucno z d1
        # ce sta meseca enaka vrne 1, ker se steje da je ta mesec delal
        if _d1 > _d2:
            d1 = _d2
            d2 = _d1
            sign = -1
        else:
            d1 = _d1
            d2 = _d2
            sign = 1

        if d1.year == d2.year:
            return ((d2.month - d1.month) + 1) * sign

        # 12 mesecev v celih letih
        months = (d2.year - d1.year -1) * 12
        # pristejem mesece v prvem letu
        months += 12 - (d1.month - 1)
        # pristejem mesece v zadnjem letu
        months += d2.month
        return months * sign

ymd1 = YMD(10,0,0)
ymd2 = YMD(2,2,6)
print ymd1 + ymd2
print ymd1 - ymd2

ymd1 = YMD(19,3,3)
ymd2 = YMD(6,4,29)
print ymd1 + ymd2
print ymd1 - ymd2

ymd1 = YMD(19,3,3)
ymd2 = YMD(6,2,2)
print ymd1 + ymd2
print ymd1 - ymd2
