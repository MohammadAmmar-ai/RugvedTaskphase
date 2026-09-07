def colemanliauindex(text):
    letter=0
    word=0
    sentence=0
    text=" "+text
    for i in range (len(text)):
        char=text[i]
        if char.isalpha():
            letter+=1
        elif char==" ":
            word+=1
        elif char=="." or char=="?" or char=="!":
            sentence+=1
    L=(letter/word)*100
    S=(sentence/word)*100
    CLI=0.0588*L-0.296*S-15.8
    grade=round(CLI)
    if grade<1:
        return 0
    return grade
s=input("Enter a sentence to check it's grade: ")
print(colemanliauindex(s))