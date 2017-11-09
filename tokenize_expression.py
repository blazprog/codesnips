import re
operand = re.compile(r'\w+')
operator = re.compile(r'[+\-*/]')
open_brace = re.compile(r"\(")
close_brace = re.compile(r'\)')

def tokenize(expression):
    # na zacetku iscem samo openarnd ali odprti oklepaj
    uncloses_braces = 0
    token_list = []
    search_expressions = [operand, open_brace]
    while True:
        for se in search_expressions:
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


if __name__ == '__main__':
    tokenize("hitrost*cas")
