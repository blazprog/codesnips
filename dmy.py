class DYM:
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
            year_increment = 2
        years = self.years = other.years + year_increment
        return DYM(years, months, days)

    def __sub__(self, other):
        other_month_increment = other_year_increment = 0
        days = self.days - other.days
        if days < 0:
            other_month_increment = 1
            days = self.days + (30-other.days)
        months = self.months - (other.months + other_month_increment)
        if months < 0:
            months = (13-other.months - other_month_increment) + self.months
            other_year_increment = 1
        years = self.years - (other.years + other_year_increment)
        return DYM(years, months, days)

    def __lt__(self, other):
        return (self.years * 365 + self.months * 30 + self.days <
                other.years * 365 + other.months * 30 + other.days)

    def __eq__(self, other):
        return(
            self.years == other.years and
            self.months == other.months and
            self.days == other.days
        )

    def __str__(self):
        return "{:02d}-{:02d}-{:02d}".format(self.years,
                                             self.months,
                                             self.days)


if __name__ == "__main__":
    d1 = DYM(10, 2, 3)
    d2 = DYM(9, 3, 20)
    print d1, d2, d1 - d2
    d1 = DYM(12, 2, 3)
    d2 = DYM(9, 1, 2)
    print d1, d2, d1 - d2
    d1 = DYM(9, 4, 3)
    d2 = DYM(9, 3, 20)
    d3 = DYM(9, 3, 20)
    print d1, d2, d1 - d2
    print d1, '<', d2, d1 < d2
    print d2, '=', d3, d2 == d3
    print d1, '>', d2, d1 > d2
