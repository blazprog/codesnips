class ContractChangeLine:
    def __init__(self, employee_name, date, description):
        self.employee_name = employee_name
        self.date = date
        self.description = description

    #Vrstice porocila zelim sortirati po zaposlenih in po datumu
    def __eq__(self, other):
        return self.employee_name == other.employee_name and \
               self.date == other.date

    def __lt__(self, other):
        print 'sorting...'
        if self.employee_name < other.employee_name:
            return True
        elif self.employee_name > other.employee_name:
            return False
        else:
            return self.date < other.date

    def __str__(self):
        return self.employee_name + ' ' + self.date

c1 = ContractChangeLine('Baaz', '2018-02-01', 'opis1')
c2 = ContractChangeLine('Boo', '2018-01-01', 'opis2')
l = []
l.append(c2)
l.append(c1)
print c1, c2
print c1.__dict__
print l
print sorted(l)
