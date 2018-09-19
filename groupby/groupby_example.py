# -*- coding: utf-8 -*-
from itertools import groupby
from operator import attrgetter

class Holidays:
    def __init__(self, code, name, hours):
        self.code = code
        self.name = name
        self.hour = hours

    def __str__(self):
        return "Holiday object {} {} {}".format(self.code, self.name, self.hour)


holidays_list = []
holidays_list.append(Holidays('a', 'Name a1', 2))
holidays_list.append(Holidays('b', 'Name b1', 3))
holidays_list.append(Holidays('c', 'Name c1', 4))
holidays_list.append(Holidays('a', 'Name a1', 5))
holidays_list.append(Holidays('b', 'Name b2', 6))
holidays_list.append(Holidays('c', 'Name c2', 7))
holidays_list.append(Holidays('d', 'Name d1', 8))
holidays_list.append(Holidays('e', 'Name e1', 9))

holidays_list.sort(key=attrgetter("code"))

groups = groupby(holidays_list, attrgetter("code"))

for k, v in groups:
    print (k, v)
    l = list(v)
    print l
    result = [l[0].name, sum([i.hour for i in l])]
    print (result)



