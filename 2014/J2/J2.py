x = int(input())
y = input()

a = "A"
b = "B"
a_count = 0
b_count = 0
for i in range(x):
    if(y[i]==a):
        a_count+=1
    if(y[i]==b):
        b_count+=1

if(a_count>b_count):
    print("A")
elif(a_count<b_count):
    print("B")
elif(a_count == b_count):
    print("Tie")