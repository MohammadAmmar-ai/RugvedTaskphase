def diamondprint(n):
    line=""
    for i in range(0,n):
        pos=n-1-i
        for j in range(0,n):
            if j>pos:
                line=line+"*"
            else :
                line = line + " "

        print(line)
        line = ""
    for i in range(0,n):
        pos=i
        for j in range(0,n):
            if j>pos:
                line = line + "*"
            else :
                line = line + " "

        print(line)
        line = ""
n = int(input("Enter the value n for shape of diamond: "))
diamondprint(n)