d = {
    1: 10,
    2: 20,
    3: 30,
    4:40,
    5:50
}
print d
l = [(0,0,{'product_id':key, 'qyt':value}) for key, value in d.items()]
print l
