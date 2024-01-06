david = 100
antonia = 100
x = int(input())
for i in range(x):
    one,two = map(int,input().split())
    if(one>two):
        antonia -= one
    if(one<two):
        david -= two

print(david)
print(antonia)