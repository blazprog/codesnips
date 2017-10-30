import operator
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

def postfixToPrefix(postfix_expr):
    stack = Stack()
    tokenList = postfix_expr.split()
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            stack.push(token)
        else: # must be operator
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push(' '.join([token, op2, op1]))
    res = ''
    while not stack.isEmpty():
        res += stack.pop()
    return res

def postfixEval(postfixExpr):
    func = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    operandStack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token in '0123456789':
            operandStack.push(int(token))
        else:
            op2 = operandStack.pop()
            op1 = operandStack.pop()
            operandStack.push(func[token](op1, op2))
    return operandStack.pop()




def main():
    while True:
        expresion = input('Vnesi infix izraz q za konec: ')
        if expresion == 'q':
            break
        postfixExpression = infixToPostfix(expresion)
        print ('Rezultat pretvorbe je: ')
        print(postfixExpression)
        print(postfixToPrefix(postfixExpression))
        print ('Rezultat izracuna je: ')
        print(postfixEval(postfixExpression))



if __name__ == '__main__':
    main()

# print(infixToPostfix("A * B + C * D"))
# print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
