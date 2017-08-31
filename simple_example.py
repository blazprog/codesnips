# -*- coding: utf-8 -*-

import sys
import pyparsing as pp

def define_parser():
    '''
    parser fro python indetifier
    '''
    first = pp.Word(pp.alphas + '_', exact=1)
    rest = pp.Word(pp.alphanums + '_')

    # The Python “+” operator is overloaded for instances of the pp.ParserElement class to mean sequence:
    # that is, the identifier parser matches what the first parser matches, followed optionally by what
    # the rest parser matches.
    python_identifier = first + pp.Optional(rest)
    return python_identifier

def get_test_string_list():
    return [
        '_lal64',
        '7skratov',
        '_55',
        'dollar'
    ] 

def main():
    testList = get_test_string_list()
    parser = define_parser()
    for test in testList:
        try:
            result = parser.parseString(test)
            print 'Match ',  result
        except pp.ParseException as e:
            print 'No match ', e


if __name__ == '__main__':
    main()


