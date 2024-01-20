x = int(input())
arr = []
for i in range(x):
    line = input().split()
    for g in range (len(line)):
        line[g] = int(line[g])
    arr.append(line)

def rotate(arr,x):
    temp = []
    for w in range (x):
        temp.append([0]*x)
    for i in range(x):
        for z in range(x):
                temp[i][z] = arr[z][x-i-1]
    return temp

while(arr[0][0] > arr[0][x-1] or arr[x-1][0] > arr[x-1][x-1] or arr[0][0]>arr[-1][0]):
     arr = rotate(arr,x)

for line in arr:
     print (" ".join(list(map(str,line))))
