# -*- coding: utf-8 -*-
# merge list of dictionarys

'''
test values:
na =  21 + 21 + 1 + 21 + 33 = 97
nb = 1 + 21 + 77 =  99
'''

def dicts_equal(d1, d2, compare_fields):
    for f in compare_fields:
        if d1[f] != d2[f]:
            return False
    # ce sem prisel do sem so vsa polja enaka
    return True

dict_list = [
    {'name': 'na', 'surname': 'sa', 'qty':21},
    {'name': 'nb', 'surname': 'sb', 'qty':1},
    {'name': 'nc', 'surname': 'sc', 'qty':121},
    {'name': 'nd', 'surname': 'sd', 'qty':29},
    {'name': 'na', 'surname': 'sa', 'qty':21},
    {'name': 'nx', 'surname': 'sx', 'qty':21},
    {'name': 'nb', 'surname': 'sb', 'qty':21},
    {'name': 'nc', 'surname': 'sc', 'qty':21},
    {'name': 'na', 'surname': 'sa', 'qty':1},
    {'name': 'na', 'surname': 'sa', 'qty':21},
    {'name': 'ne', 'surname': 'se', 'qty':21},
    {'name': 'nf', 'surname': 'sf', 'qty':21},
    {'name': 'ng', 'surname': 'sg', 'qty':21},
    {'name': 'ne', 'surname': 'se', 'qty':21},
    {'name': 'nf', 'surname': 'sf', 'qty':21},
    {'name': 'ng', 'surname': 'sg', 'qty':21},
    {'name': 'nw', 'surname': 'sw', 'qty':21},
    {'name': 'nc', 'surname': 'sc', 'qty':21},
    {'name': 'nx', 'surname': 'sx', 'qty':21},
    {'name': 'na', 'surname': 'sa', 'qty':33},
    {'name': 'nb', 'surname': 'sb', 'qty':77},
]

compare_fields = ('name', 'surname')
sum_field = 'qty'


def shrink_list(dict_list, compare_fields, sum_field):

    list_len = len(dict_list)
    current_element = 0
    while current_element < list_len:
        del_indexes = []
        for compare_element in range(current_element + 1, list_len):
            if dicts_equal(dict_list[current_element], dict_list[compare_element], compare_fields):
                dict_list[current_element][sum_field] += dict_list[compare_element][sum_field]
                del_indexes.insert(0,compare_element) # brisati moram od najvisjega indeksa nazaj
        for i in del_indexes:
            dict_list.pop(i)
        current_element += 1
        list_len = len(dict_list)


shrink_list(dict_list, compare_fields, sum_field)
for d in (dict_list):
    print (d)
