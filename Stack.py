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