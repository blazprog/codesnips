class Employee:
    def __init__(self, key, name, street, zip, city):
        self.key = key
        self.name = name
        self.street = street
        self.zip = zip
        self.city = city
        self.identification_id = ''
        self.tax_id = ''
        self.other_id = ''
        self.gender = 'male'
        self.birthday = ''
        self.place_of_birth = ''
        self.daily_commuting_expenses = 2
        self.education_level = ''
        self.profesion = ''

class EmployeeContract:
    def __init__(self, key, name, date_start, date_end, past_work):
        self.key = key
        self.name =name
        self.date_start = date_start
        self.date_end = date_end
        self.past_work = past_work
