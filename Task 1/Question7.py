def fibonacciseries(n):
    first=0
    second=1
    count=0
    while count<=n:
        print(first)
        next_term=first+second
        first=second
        second=next_term
        count+=1
print("Enter a number to print fabonacci series till there")
x=int(input())
fibonacciseries(x)