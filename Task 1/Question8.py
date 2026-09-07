def wordpartition(n,s):
    length=len(s)

    if length%n!=0:
        print("The word cannot be broken into equal parts")
        return

    else:
        i=0
        parts=[]
        while i<length:
            piece=""
            for j in range(i,i+n):
                piece+=s[j]
            parts.append(piece)
            i+=n
        for i in range(len(parts)):
            print(parts[i],end=" ")

s=input("Enter a string")
n=int(input("Enter a number it should be broken into"))
wordpartition(n,s)
