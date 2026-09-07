def sort_and_count(s):
    chars=[]
    for i in range(len(s)):
        chars.append(s[i])

    n=len(chars)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if chars[j]>chars[min_index]:
                min_index=j
        temp=chars[i]
        chars[i]=chars[min_index]
        chars[min_index]=temp

    sorted_string=""
    for i in range(n):
        sorted_string+=chars[i]
    print(sorted_string,"is the sorted string")

    counts={}
    for i in range(len(sorted_string)):
        ch=s[i]
        if ch in counts:
            counts[ch]+=1
        else:
            counts[ch]=1
    for ch in counts:
        print(ch,":",counts[ch])

s=input("Enter string:")
sort_and_count(s)

