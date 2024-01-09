x = int(input())
arr = []
for i in range(x):
    y,z = input().split()
    z = int(z)
    arr.append([y,z])
    
print(arr[0][1])