# modul za prestevilcenje potnih nalogov
import re

to_sample = "PN-PO042-17-100"

to_regex = r"(?P<prefix>PN-PO\d\d\d-\d\d-)(?P<sequence>\d{3})"

m = re.search(to_regex, to_sample)
if m:
    print 'Found match {}'.format(m.group())
    print 'Found group in match {}'.format(m.group('sequence'))
else:
    print 'Match not found'

def increment_sequence(match):
    prefix = match.group('prefix')
    sequence = int(match.group('sequence')) + 1
    return prefix + '{:3d}'.format(sequence)
    
def get_increment_function(inc):
    def increment_match(match):
        prefix = match.group('prefix')
        sequence = int(match.group('sequence')) + inc
        return prefix + '{:3d}'.format(sequence)
    return increment_match

inc_foo = get_increment_function(301)

new_to_number = re.sub(to_regex, inc_foo, to_sample)
print new_to_number


# besedi, ki sledi @ doda index crke e 
string = "The quick @red fox @jumps over the @lame brown dog."
def my_replace(match):
    match = match.group()
    print 'match', match
    return match + str(match.index('e'))

print re.sub(r'@\w+', my_replace, string)
