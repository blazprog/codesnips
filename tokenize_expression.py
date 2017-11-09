import re
operand = re.compile(r'[A-Za-z]+')
number = re.compile(r'\d+(\.\d+|\d*)')
operator = re.compile(r'[+\-*/]')
open_brace = re.compile(r"\(")
close_brace = re.compile(r'\)')

def tokenize(expression):
    original_expression = expression
    # na zacetku iscem samo openarnd ali odprti oklepaj
    search_expressions = [operand, number, open_brace]
    unclosed_braces = 0
    token_list = []
    while len(expression):
        found = False
        for se in search_expressions:
<<<<<<< HEAD
            print se
            match = se.match(expression)
            if match:
                print match, match.group()
                token_list.append(match.group())
                end = match.end()
                expression = expression.strip()
                expression = expression[end:]
                print expression
                if not len(expression):
                    break
                if se == open_brace:
                    uncloses_braces +=1
                    search_expressions = [operand]
                if se == close_brace:
                    uncloses_braces -=1
                    if uncloses_braces < 0:
                        raise ValueError('Braces does not match')
                    search_expressions = [operator]
                elif se == operand:
                    print 'tu sem'
                    search_expressions = [operator, close_brace]
                elif se == operator:
                    search_expressions = [operator, close_brace]
            else:
                break

    print token_list
=======
            print 'matching', expression
            match = se.match(expression)
            if match:
                print 'match string', match.group()
                found = True
                token_list.append(match.group())
                end = match.end()
                expression = expression[end:].strip()
                if se == open_brace:
                    unclosed_braces +=1
                    search_expressions = [operand, number]
                if se == close_brace:
                    unclosed_braces -=1
                    if unclosed_braces < 0:
                        raise ValueError('Braces does not match in %s ' %
                                         original_expression )
                    search_expressions = [operator, close_brace]
                elif se == operand:
                    search_expressions = [operator, close_brace]
                elif se == number:
                    search_expressions = [operator, close_brace]
                elif se == operator:
                    search_expressions = [operand, number, open_brace]
                break # match found -> exit for

        if not found:
            raise ValueError('Error in expression %s ' % original_expression)
    if unclosed_braces:
        raise ValueError('Braces does not match in %s' % original_expression)
    return token_list
>>>>>>> 741af30f26fa204985b0797e1a6418bd0d9604e5


if __name__ == '__main__':
    try:
        print tokenize("22 + 33")
    except ValueError as e:
        print e
    try:
        print tokenize("yy + 22.2 + (xx *(dd+11))")
    except ValueError as e:
        print e
    try:
        print tokenize("hitrost*cas")
    except ValueError as e:
        print e
    try:
        print tokenize("yy + (xx *dd)")
    except ValueError as e:
        print e
    try:
        print tokenize("yy + (xx *(dd)")
    except ValueError as e:
        print e
