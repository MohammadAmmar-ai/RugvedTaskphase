def caeserencrypt(text,shift):

    result=""
    for i in range(len(text)):
        ch=text[i]

        if ch>='a' and ch<='z':
            base=ord('a')
            newch=(ord(ch)-base+shift)%26+base
            result+=chr(newch)
        elif ch>='A' and ch<='Z':
            base=ord('A')
            newch=(ord(ch)-base+shift)%26+base
            result+=chr(newch)
        else:
            result+=ch
    print(result)

text=input("Enter a word to ecrypt: ")
shift=int(input("Enter a shift number: "))
caeserencrypt(text,shift)