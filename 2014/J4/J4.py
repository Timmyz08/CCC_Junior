no_of_friend = int(input()) 
friendList = []
for i in range(no_of_friend): 
    friendList.append(i+1)

rounds = int(input()) 
for i in range(rounds):
    r = int(input()) 
    selected_friends = []
    for j in range(len(friendList)): 
        if (j+1)%r != 0:
            selected_friends.append(friendList[j])
            friendList = selected_friends

for i in friendList: 
    print(i)