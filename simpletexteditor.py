"""Link to the problem :-https://www.hackerrank.com/challenges/simple-text-editor
@Author : Naveen Chaudhary"""
def texteditor():
    s = [] 
    str2 = ""
    case = int(input())
    for test in range(0,case):
        
         
        stri = input().split()
        choice = int(stri[0])
        if  choice == 1:
            str2 = str2 + stri[1]
            s.append(str2)
        elif choice == 2:
            k = int(stri[1]) 
            str2 = str2[0 :len(str2) - k]
            s.append(str2)
        elif choice == 3:
            char = int(stri[1])
            if (char - 1) < len(str2):
                print(str2[char-1])
        elif choice == 4:
            s.pop()
            if len(s) > 0:
                str2 = s[len(s) - 1]
            else:
                str2 = ""
            
            
            
texteditor()
            