def hillclimb(n):
    digits=[int(d) for d in str(n)]
    length=len(digits)
    i=0
    while i<length and digits[i]<digits[i+1]:
        i=i+1

    peak=i
    if peak==0 or peak==length-1:
        return False
    while i<length and digits[i]>digits[i-1]:
        i+=1

    return i==length-1

n=input("Enter a number:")
print(hillclimb(n))