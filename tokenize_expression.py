import re
operand = re,compile(r'\w+')
operator = re.compile(r['+-*/'])
open_brace = re.compile(r'(')
close_brace = re.compile(r')')


def tokenize(expression):
    # na zacetku iscem samo openarnd ali odprti oklepaj
    search_expressions = [operand, open_brace]
