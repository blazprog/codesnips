SORUCE_FILE = '/home/blaz/projekti/odoo/relax_data/prazniki'
TARGET_FILE = '/home/blaz/projekti/odoo/relax_data/prazniki_urna_postavka.csv'
# Read from file and write to file
try:
    with open(SORUCE_FILE) as fin:
        with open(TARGET_FILE, "w") as fout:
            for line in fin:
                f = line.split('|')
                davcna = f[0].strip()
                ure = float(f[2].strip())
                znesek = f[3].strip().replace(',', '.')
                znesek = round(float(znesek), 2)
                print(davcna, znesek, ure) 
                out_line = "||{}|{}\n".format(davcna, znesek/ure)
                print (out_line)
                fout.write(out_line)
except EnvironmentError as err:
    print(err)
    
