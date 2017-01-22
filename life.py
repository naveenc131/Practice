def life():
    result = True
    list =[]
    while result :
        number = int(input())
        assert type(number) == int
        if number== 42:
            result = False
        else :
            list.append(number)
    for number in list:
        print (number)
life()
        