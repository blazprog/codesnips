from sys import stdin
s = raw_input("Ali naj sortiram D-N")
if s.upper() == 'D':
    for line in stdin:
        print ' '.join(sorted(line.split()))
