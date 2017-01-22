"""
ONP - Transform the Expression
#stack
Transform the algebraic expression with brackets into RPN form (Reverse Polish Notation). Two-argument operators: +, -, *, /, ^ (priority from the lowest to the highest), brackets ( ). Operands: only letters: a,b,...,z. Assume that there is only one RPN form (no expressions like a*b*c).
input

t [the number of expressions <= 100]
expression [length <= 400]
[other expressions]
Text grouped in [ ] does not appear in the input file.

Output

The expressions in RPN form, one per line.
Example

Input:
3
(a+(b*c))
((a+b)*(z+x))
((a+t)*((b+(a+c))^(c+d)))

Output:
abc*+
ab+zx+*
at+bac++cd+^*



@Author : Naveen Chaudhary
"""

class StackClass:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def peek(self):
        return self.items[-1:][0]

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)
        return 0
def balanced(inputstr):
    stack = []
    for i in inputstr:
            if i == '(':
                    stack += i
            elif i == ')':
                    if stack.pop() == '(':
                            continue
                    else:
                            return False
    if len(stack) > 0:
            return False
    return True
   
def infixtopostfix():
    cases = int(input())
    assert cases < 100 ,"Cases <100 "
    inputs = []
    for t in range(0,cases):
        expression = input()
        assert len(expression) <= 400,"expression < 400"
        inputs += [expression]
    
    s = StackClass()
    out=[]
    prec={}
    prec['^']=4
    prec['/']=3
    prec['*']=3
    prec['+']=2
    prec['-']=2
    prec['(']=1
    oplst=['/','*','+','-']
    for str in inputs :
        if balanced(str):

            for item in str:
                if item in "qwertyuiopasdfghjklzxcvbnm" or item in "0123456789":
                    out.append(item)
                elif item == '(':
                    s.push(item)
                elif item == ')':
                    top = s.pop()
                    while top != '(':
                        out.append(top)
                        top = s.pop()
                else:
                    while (not s.isEmpty()) and (prec[s.peek()] >= prec[item]) :
                        out.append(s.pop())
                    s.push(item)
            while not s.isEmpty() :
                        out.append(s.pop())
            for i in out:
                print (i,end="")
            print()
        out = []
infixtopostfix()