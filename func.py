from pyparsing import Word, alphas, ParseException, Literal, CaselessLiteral \
, Combine, Optional, nums, Or, Forward, ZeroOrMore, StringEnd, alphanums

from numpy import median as avg

lpar  = Literal( "(" ).suppress()
rpar  = Literal( ")" ).suppress()
comma = Literal(',').suppress()
number = Word(nums).setParseAction(lambda token: int(token[0]))
func_sum = Literal('SUM').setParseAction(lambda: sum)
func_avg = Literal('AVG').setParseAction(lambda: avg)
func = func_sum | func_avg
arguments = number + ZeroOrMore(comma + number)
pattern = func + lpar + arguments + rpar


parse_expression = "AVG(3, 4, 5, 6)"
result = pattern.parseString(parse_expression)
print result
func = result[0]
args = result[1:]
print func(args)
