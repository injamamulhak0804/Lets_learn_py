def anagram_check(s1, s2):
    s1len = len(s1)
    s2len = len(s2)
    count = 0
    if(s1len == s2len):
        for i in range (s1len):
            for j in range(s2len):
                    count += 1
                    break
        # print(s1len)
        if(count == s1len):
            print("It is a anagram")
        else:
            print("Not an anagramss")
    else:
        print("Not an anagram asa")

anagram_check("hello", "elloh")