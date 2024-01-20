x = int (input())
yesterday = input()
today = input()
counter = 0
for i in range(x):
    if(yesterday[i] == "C" and today[i] == "C"):
        counter += 1
print(counter)