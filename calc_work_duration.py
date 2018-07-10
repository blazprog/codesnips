# -*- coding: utf-8 -*-
import datetime
import calendar
import re

class AllWorkingPeriods():
    def __init__(self):
        self.working_periods = []
        self.years = 0
        self.months = 0
        self.days = 0

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

    def return_aniversary_date(self, years, previous_work):
        '''
        :param years: number of years to serach 
        :param previous_work: work till working periods
        :return:  date when number of years matched
        '''
        search_period = YMD(years, 0, 0)
        pattern = r"(\d{1,2})-(\d{1,2})-(\d{1,2})"
        m =  re.match(pattern, previous_work)
        if m:
            g = m.groups()
            period_before = YMD(int(g[0]), int(g[1]), int(g[2]))
        if period_before >= search_period:
            return False

        time_to_award = search_period - period_before
        tmp_ymd = period_before
        calc_wp = False
        for wp in self.working_periods:
            calc_wp = wp
            wp_ymd = YMD(wp.years, wp.months, wp.days)
            tmp_ymd += wp_ymd
            if tmp_ymd > time_to_award:
                break

        time_to_find = search_period - tmp_ymd
        # koliko casa mora delati v periodi calc_wp, da bo izpolnil time_to_find
        return calc_wp.time_passed_date(time_to_find.years, time_to_find.months, time_to_find.days)


    def add_previous_periods(self, period):
        '''
        :param period:strng v obliki ll-mm-yy 
        :return: vrne trenutno vrednost, povecano za param kot string
        '''
        years =  months =  days = 0
        pattern = r"(\d{1,2})-(\d{1,2})-(\d{1,2})"
        if period:
            m =  re.match(pattern, period)
            if m:
                g = m.groups()
                years = int(g[0])
                months = int(g[1])
                days = int(g[2])
        y = self.years + years
        m = self.months + months
        d = self.days + days
        m += d // 30
        d = d % 30
        y += m // 12
        m = m % 12
        return "{:02d}-{:02d}-{:02d}".format(y, m, d)

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
            wd = int(round((full_months * 30 + days) * float(working_hours) / float(WorkingPeriod.FULL_TIME),0))
            # todo: ce je vec kot 0.6 zaokrozim navzgor sicer navzdol
            self.years = wd // 365
            wd = wd % 365
            self.months = wd // 30
            self.days = wd % 30

    def time_passed_date(self, years, months, days):
        '''
        
        :param years: 
        :param months: 
        :param days: 
        :return: Vrne datum, v katerem bo v tej periodi minil cas v parametru
        '''
        if self.working_hours == WorkingPeriod.FULL_TIME:
            # ce dela za polni delovni cas
            return self.date_from + datetime.timedelta(years = years) + \
                                    datetime.timedelta(months=months) + \
                                    datetime.timedelta(days=days)

        else:
            koef = float(self.working_hours) / float(WorkingPeriod.FULL_TIME),
            days = int((years * 365 + months * 30 + days) * koef)
            return self.date_from + datetime.timedelta(days=days)

    def __str__(self):
        return "{:02d}-{:02d}-{:02d}".format(self.years,
                                             self.months,
                                             self.days)


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
            year_increment = 2
        years = self.years = other.years + year_increment
        return YMD(years, months, days)

    def __sub__(self, other):
        days = self.days - other.days
        if days < 0:
            other_month_increment = 1
            days = self.days + (30-other.days)
        months = self.months - (other.months + other_month_increment)
        if months < 0:
            months = (13 - other.months  - other_month_increment) + self.months
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

