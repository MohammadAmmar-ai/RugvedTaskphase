def anagramcheck():
    word1=input("Enter a word")
    word2=input("Enter another word")

    letter1=[char for char in word1]
    letter2=[char for char in word2]

    letter1.sort()
    letter2.sort()

    if letter1==letter2:
        print(word1,"and",word2,"are anagrams")
    else:
        print(word1,"and",word2,"are not anagrams")
anagramcheck()