x = int(input())
y = int(input())
arr = []
for i in range(y):
    arr.append(int(input()))

ans = sorted(arr)
index = 0
sum = ans[0]
while (sum<=x):
    index +=1
    sum+=ans[index]
print(index)
