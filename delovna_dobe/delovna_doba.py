import datetime
import re
import calendar
from __future__ import division # da mi deljenje celih stevil vrne float

def decode_duration(duration=False):
    years = months = days = 0
    pattern = r"(\d{1,2})-(\d{1,2})-(\d{1,2})"
    if duration:
        m = re.match(pattern, duration)
        if m:
            g = m.groups()
            years = int(g[0])
            months = int(g[1])
            days = int(g[2])
    return [years, months, days]





def calc_date_duration(date_from=False, date_to=False, past_work=False):
    '''

    :param date_from: 
    :param date_to: 
    :param past_work: 
    :return: list s podatki let, mesecev, dni delovne dobe 
    '''
    _month_day = [31, -1, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    _date_from = date_from             #datetime.strptime(date_from, '%Y-%m-%d')
    _date_to = date_to                 # and datetime.strptime(date_to, '%Y-%m-%d') or datetime.today()
    _increment = 0
    if _date_from.day > _date_to.day:
        _increment = _month_day[_date_from.month - 1]
    if _increment == -1:
        if calendar.isleap(_date_from.year):
            _increment = 29
        else:
            _increment = 28
    if _increment != 0:
        _days = _date_to.day + _increment - _date_from.day
        _increment = 1
    else:
        _days = _date_to.day - _date_from.day
        _increment = 0

    if _date_from.month + _increment > _date_to.month:
        _months = (_date_to.month + 12) - (_date_from.month + _increment)
        _increment = 1
    else:
        _months = _date_to.month - (_date_from.month + _increment)
        _increment = 0
    _years = _date_to.year - (_date_from.year + _increment)

    if past_work:
        _past_years, _past_months, _past_days = decode_duration(past_work)
        if _past_days + _days > 30:
            _days += _past_days - 30
            _increment = 1
        else:
            _days += _past_days
            _increment = 0
        if _past_months + _months + _increment >= 12:
            _months += _past_months + _increment - 12
            _increment = 1
        else:
            _months += _past_months + _increment
            _increment = 0
        _years += _past_years + _increment

    return [_years, _months, _days]
    # -*- coding: utf-8 -*-


def main():
    date_from = datetime.date(1998, 12, 10)
    date_to = datetime.date(2018, 2, 1)

    working_period = calc_date_duration(date_from, date_to)
    delta = date_from-date_to
    diff = abs(delta.days)
    wpdays = working_period[0] * 365 + int(working_period[1] * (365/12)) + working_period[2]
    # wpdays = working_period[0] * 365 + working_period[1] * 30 + working_period[2]
    print (working_period)
    print (diff,  wpdays)
    years = diff // 365
    r = diff % 365
    months = r // 30
    days = r % 30
    print ("{}-{}-{}")
    print ("Calculated days ", years, months, days)
    s = "{}"
    print ("Calculated days ", years, months, days)

class AllWorkingPeriods():
    def __init__(self):
        self.working_periods = []

    def add_working_period(self, date_from, date_to, working_hours):
        self.working_periods.append(date_from, date_to, working_hours)

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

class WorkingPeriod:
    FULL_TIME = 8
    def __init__(self, date_from, date_to, working_hours ):
        self.date_from = date_from
        self.date_to = date_to
        self.working_hours = min(working_hours, WorkingPeriod.FULL_TIME)

        full_months = max(0, Month.count_months(d_first_full, d_last_full))
        firs_month_days = (30-d1.day) + 1

        last_day_in_month = calendar.monthrange(d2.year, d2.month)[1]
        if d2.day == last_day_in_month:
            last_month_days = 30
        else:
            last_month_days = 30 - (30 - d2.day)

        full_months += (firs_month_days + last_month_days) // 30
        days = (firs_month_days + last_month_days) % 30

        if working_hours == WorkingPeriod.FULL_TIME:
            self.years = full_months // 12
            self.months = full_months % 12
            self.days = days
        else:
            wd = int(round((full_months * 30 + days) * working_hours / WorkingPeriod.FULL_TIME,0))
            # ce je vec kot 0.6 zaokrozim navzgor sicer navzdol
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
        day = 1
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
            year = d.year = 1
        else:
            year = d.year

    def __init__(self, year, month , day=1):
        self.year = year
        self.month = month
        self.day = day

    def date(self):
        return datetime.date(self.year, self.month, self.day)

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
            return (d2.month - d1.month) + 1

        # 12 mesecev v celih letih
        months = (d2.year - d1.year -1) * 12
        # pristejem mesece v prvem letu
        months += 12 - (d1.month - 1)
        # pristejem mesece v zadnjem letu
        months += d2.month
        return months * sign


if __name__ == "__main__":
    # main()
    d1 = datetime.date(2017, 3, 15)
    d2 = datetime.date(2019, 5, 3)

    d_first_full = Month.next_month_firs_day(d1)
    d_last_full = Month.previous_month_last_day(d2)

    full_months = max(0, Month.count_months(d_first_full, d_last_full))
    firs_month_days = (30-d1.day) + 1
    last_day_in_month = calendar.monthrange(d2.year, d2.month)[1]
    if d2.day == last_day_in_month:
        last_month_days = 30
    else:
        last_month_days = 30 - (30 - d2.day)

    full_months += (firs_month_days + last_month_days) // 30
    days = (firs_month_days + last_month_days) % 30

    print ('Worktime period',
           "{:02d}-{:02d}-{:02d}".format(full_months // 12, full_months % 12, days))


    print (d_first_full)
    print (d_last_full)
    print ("Prvi je majsi od zadnjega", d_first_full < d_last_full)

    r1 = Month.next_month_firs_day(datetime.date(2019, 6, 15))
    r2 = Month.previous_month_last_day(datetime.date(2019, 8, 3))
    print ("Meseca", r1, ' in ', r2, " sta enaka ", r1  ==  r2)
    print  ('Stevilo mesecev je', Month.count_months(d_first_full, d_last_full))
