from pyparsing import (alphanums, alphas, CharsNotIn, Forward,
Group, hexnums, OneOrMore, Optional, ParseException,
ParseSyntaxException, Suppress, Word, ZeroOrMore, restOfLine)


def accumulate(tokens):
    key, value = tokens
    key_values[key] = value

key_values = {}
left_bracket, right_bracket, equals = map(Suppress, "[]=")
ini_header = left_bracket + CharsNotIn("]") + right_bracket
key_value = Word(alphanums) + equals + restOfLine
key_value.setParseAction(accumulate)
comment = "#" + restOfLine
parser = OneOrMore(ini_header | key_value)
parser.ignore(comment)


parser.parseFile('songs')

for k,v in key_values.items():
    print k, v
