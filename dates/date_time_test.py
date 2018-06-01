# -*- coding: utf-8 -*-

# vsi razredi za delo z datumi so v datetime modulu
import datetime


#1) samo datum

d = datetime.date(year=2018, month=4, day=3)
print d.year, d.month, d.day

today = datetime.date.today()
print today.year, d.month, d.day
print today.strftime('%Y-%m-%d') # v ansi formatu yyyy-mm-dd
print today.strftime('%d.%m.%Y') # v slovenskem formatu dd.mm.yyyy

print "uporaba timedelta za povecevanje, pomanjsanje datuma"
one_day = datetime.timedelta(days=1)
tomorow = today + one_day
yesterday = today - one_day
print yesterday, '\n', today, '\n', tomorow


print 'Enumeracija dni med dvema datuma'
s_d1 = '2011-02-03'
s_d2 = '2011-03-03'
d_d1 = datetime.datetime.strptime(s_d1, "%Y-%m-%d").date()
d_d2 = datetime.datetime.strptime(s_d2, "%Y-%m-%d").date()
nb_of_days = (d_d2 - d_d1).days
one_day = datetime.timedelta(days=1)
current_date = d_d1
for x in range(nb_of_days+1):
    print current_date
    current_date += one_day

print 'Konec enumeracije'

import calendar
print "Uporaba koledarja"
print calendar.isleap(2018) # --> False

print 'Stevilo dni v mesecu s pomocjo funkcije monthrange'
print 'Funkcija month range vrne tuple. Prvi element je prvi dan v mesecu (pon, tor....)'
print 'Drugi element pa je stevilo dni v mesecu'
print calendar.monthrange(year=2018, month=4) # vrne (6, 30), ker je 1.4.2018 nedelja (6)

"""
Funkcija itermonthdays, ki vrne vse dneve za podan mesec in leto.
Vkljuceni so tudi dnevi pred zacetkom in koncem, tako da je vedno
cel teden. 
"""
c = calendar.Calendar()
for day in c.itermonthdates(year=2018, month=5):
    print type(day), day

'''
Ce hocem dobiti samo datume znotraj meseca
'''
print 'Samo datumi znotraj aprila'
print '=========================='
for day in [dt for dt in c.itermonthdates(year=2018, month=4) if dt.month == 4]:
    print type(day), day, day.weekday(), day.strftime("%A")


'''
timezone
'''
import pytz
for tz in pytz.common_timezones:
    print tz

print type(pytz.common_timezones)

# datetime v UTC timezone, vendar brez timezone informacije
d_utc = datetime.datetime.utcnow()
# datetime v localnem timezone, vendar brez timezone informacije
d_current = datetime.datetime.now()
print d_utc, d_current, 'difference', (d_utc - d_current).total_seconds()

# bolje je vedno uporabljati datetime objekt, ki vsebuje informacijo o timezone
LOCAL_TZ = pytz.timezone('Europe/Ljubljana')
MOSCOW_TZ =pytz.timezone('Europe/Moscow')

# timezone dodam v konstruktorju
d_tz_aware_utc = datetime.datetime.now(tz=pytz.UTC)
d_tz_aware_local = datetime.datetime.now(tz=LOCAL_TZ)
print d_tz_aware_utc, d_tz_aware_local, 'difference', (d_tz_aware_utc-d_tz_aware_local).total_seconds()

LOCAL_TZ = pytz.timezone('Europe/Ljubljana')
MOSCOW_TZ =pytz.timezone('Europe/Moscow')
time_ljubljana = datetime.datetime.now(tz=LOCAL_TZ)
time_moscow = datetime.datetime.now(tz=MOSCOW_TZ)
print 'time in Ljubljana', time_ljubljana,'tz info', time_ljubljana.tzinfo
print 'time in Moscow', time_moscow, 'tz info', time_moscow.tzinfo

print 'Pretvarjane med timezone'
convert_to_moscow = time_ljubljana.astimezone(MOSCOW_TZ)
print "Local converted to Moscow ", convert_to_moscow

'''
Najvecji in najmansi mozni datum
'''
date_min = datetime.date.min
date_max = datetime.date.max

print 'Najmanjsi datum', date_min, str(date_min)
