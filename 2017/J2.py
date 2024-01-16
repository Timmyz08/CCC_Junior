def takeinput():
    y = int(input())
    x = int(input())
    return y,x
def getanswer(y,x):
    ans = 0
    temp = 0
    for i in range (x+1):
        temp = y*(10**i)
        ans +=temp

    return(ans)
y,x = takeinput()
print(getanswer(y,x))