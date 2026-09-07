


def luhnscardnumber(number):
    digits=[]
    for digit in range(len(number)):
        digits.append(int(number[digit]))
    n=len(digits)
    position=0
    total=0
    for i in range(n-1,-1,-1):
        digit=digits[i]
        if position%2==1:
            digit=digit*2
            if digit>9:
                digit=digit-9
        total+=digit
        position+=1
    if total%10==0:
        return True
    else:
        return False
cardnumber=input("Enter a card number: ")
if luhnscardnumber(cardnumber):
    print("It is a valid card number.")
else:
     print("It is NOT a valid card number.")


