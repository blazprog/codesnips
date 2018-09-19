# -*- coding: utf-8 -*-
import erppeek
import datetime


def main():
    #server = 'http://localhost:8069'
    #db ='relax_2018_07_13'
    #server = '10.0.0.7:8069'

    server = 'http://odoo.relax.si:8069'
    db ='Relax'

    user='admin'
    password='Mentis2015#'

    api = erppeek.Client(server, db, user, password)
    holidays_obj = api.model('hr.holidays')

    for i in (1,2, 3, 4, 5, 6,7, 8, 10, 11, 13, 16, 17, 22, 23, 24, 25, 26, 27, 28, 29, 30):
        date_from = "2018-06-{:02d}".format(i)
        d = datetime.datetime.strptime(date_from, '%Y-%m-%d')
        if not d.weekday() in (5,6):
            print (date_from)
            print (holidays_obj.create({
                "name" : 'Bolniški dopusti-urna odsotnost',
                "holiday_status_id" : 18,
                "holiday_type" : 'employee',
                "employee_id" : 12,
                "department_id" :  9,
                "date_from" : date_from,
                "leave_duration_hours" : 4
            }))



main()
