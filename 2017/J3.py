word = input()
temp = word
def getparallal(word,temp):
    for i in range(len(word)):
        for x in range (i+1):
            temp = word[x:len(word)-i+x]
            if temp == temp[::-1]:
                return len(temp)
ans = getparallal(word,temp)
print(ans)





