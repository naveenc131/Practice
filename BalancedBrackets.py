"""Link to the Problem :- https://www.hackerrank.com/challenges/balanced-brackets
@Author :- Naveen Chaudhary"""
#!/bin/python3
class Stack:

    def __init__(self):
        self.items = []

    def isempty(self):
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
    

def parchecker():
    t = int(input().strip())
    for a0 in range(t):
        str = input().strip()
        s = Stack()
        i = 0
        balanced = True
        while i < len(str) and balanced:
           item = str[i]
           if item in "{[(":
                s.push(item)
           else :
                if s.isempty():
                    balanced = False
                else:
                     top = s.pop()
                     if not matches(top,item):
                        balanced = False
           i = i + 1
        if s.isempty() and balanced:
                    print("YES")
        else:
                    print("NO")
   
def matches(open,close):
    opens = "{(["
    closes = "})]"
    return opens.index(open) ==  closes.index(close)
                
parchecker()
    