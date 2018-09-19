imena = '/home/blaz/demo_place/imena.csv'
priimki = '/home/blaz/demo_place/priimki.csv'

def process_line(line):
    l = line.split('\t')
    print (l)

try:
    with open(filename) as fh:
        for line in fh:
            process_line(line)
except EnvironmentError as err:
    print(err)


