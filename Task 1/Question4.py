def selectionsort(n):
    digit= [int(d) for d in str(n)]

    for i in range(len(digit)):
        min = i
        for j in range(i+1,len(digit)):
            if digit[j]<digit[min]:
                min=j
        temp=digit[i]
        digit[i]=digit[min]
        digit[min]=temp
    print(digit)
n=input("Enter a number")
selectionsort(n)