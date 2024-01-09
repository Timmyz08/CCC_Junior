count = 0
for i in range(6):
    x = input()
    if(x == "W"):
        count+=1

if(count == 5 or count == 6):
    print("1")
if(count == 3 or count == 4):
    print("2")
if(count == 1 or count == 2):
    print("3")
if(count == 0):
    print("-1")