x = int(input())
arr = []
for i in range(x):
    y,z = input().split()
    z = int(z)
    arr.append([y,z])

sindex = 0
rindex = 0
windex = 0
timer = 0

for i,n  in arr:
    timer+=1
    if(i=="R"):
        rindex = i
    elif(i == "W"):
        windex = i
    elif(i == "S"):
        sindex = i
    

