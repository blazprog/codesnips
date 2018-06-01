import re
pattern = r"(\d{1,2})-(\d{1,2})-(\d{1,2})"
test = "12-20-20"

while True:
    test = raw_input("Vnesi testni string ")
    if test == 'q':
        break
    m =  re.match(pattern, test)
    if m:
        l, m, d = (int(v) for v in m.groups())
        print 'Leta ', l 
        print 'Meseci ', m
        print 'Dnevi ', d
    else:
        print 'No match'

