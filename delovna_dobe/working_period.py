# -*- coding: utf-8 -*-
import datetime
import calendar

class AllWorkingPeriods():
    def __init__(self):
        self.working_periods = []

    def add_working_period(self, date_from, date_to, working_hours):
        self.working_periods.append(WorkingPeriod(date_from, date_to, working_hours))

    def calculate_work_periods(self):
        self.years = 0
        self.months = 0
        self.days = 0
        for wp in self.working_periods:
            self.years += wp.years
            self.months += wp.months
            self.days += wp.days

        self.months += self.days // 30
        self.days = self.days % 30

        self.years += self.months // 12
        self.months = self.months % 12

    def __str__(self):
        return "{:02d}-{:02d}-{:02d}".format(self.years,
                                             self.months,
                                             self.days)


class WorkingPeriod:
    FULL_TIME = 8
    def __init__(self, date_from, date_to, working_hours ):
        self.date_from = date_from
        self.date_to = date_to

        self.working_hours = min(working_hours, WorkingPeriod.FULL_TIME)

        first_full = Month.next_month_firs_day(self.date_from)
        last_full = Month.previous_month_last_day (self.date_to)
        # ce je zacetni in koncni datum znotraj istega meseca potem mi mora zaradi pravilnosti racunanja
        # full_months biti -1
        if date_to.year == date_from.year and date_to.month == date_from.month:
           full_months = -1
        else:
            full_months = max(0, Month.count_months(first_full, last_full))
        firs_month_days = (30-date_from.day) + 1

        last_day_in_month = calendar.monthrange(date_to.year, date_to.month)[1]
        if date_to.day == last_day_in_month:
            last_month_days = 30
        else:
            last_month_days = date_to.day

        full_months = full_months +   (firs_month_days + last_month_days) // 30
        days = (firs_month_days + last_month_days) % 30

        if working_hours == WorkingPeriod.FULL_TIME:
            self.years = full_months // 12
            self.months = full_months % 12
            self.days = days
        else:
            wd = int(round((full_months * 30 + days) * float(working_hours) / float(WorkingPeriod.FULL_TIME,0)))
            # todo: ce je vec kot 0.6 zaokrozim navzgor sicer navzdol
            self.years = wd // 365
            wd = wd % 365
            self.months = wd // 30
            self.days = wd % 30

    def __str__(self):
        return "{:02d}-{:02d}-{:02d}".format(self.years,
                                             self.months,
                                             self.days)


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

if __name__ == '__main__':
    pass
    working_times = (
        (datetime.date(2015, 12, 1), datetime.date(2016, 1, 31), 8),
        (datetime.date(2015, 2, 1), datetime.date(2015, 2, 1), 8),
        (datetime.date(2009, 3, 4), datetime.date(2016, 1,10), 8),
        (datetime.date(2009, 3, 4), datetime.date(2016, 11,10), 8),
        (datetime.date(2015, 3, 1), datetime.date(2015, 4, 1), 8),
    )
    for t in working_times:
        wt = WorkingPeriod(*t)
        print str(wt)

    all_wp = AllWorkingPeriods()
    for t in working_times:
        all_wp.add_working_period(*t)
    all_wp.calculate_work_periods()
    print '------------'
    print str(all_wp)

