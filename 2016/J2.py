value = 0
counter = 0
for i in range(4):
    arr = []
    arr = map(int,input().split())
    if(value == sum(arr)):
        counter +=1
    value = sum(arr)
#counter = 3
    


    