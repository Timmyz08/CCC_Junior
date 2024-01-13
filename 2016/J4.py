arr = []
x = input().replace(":"," ")
arr = list(map(int,x.split()))

time = 120
ans = 0
if((arr[0]+2)*60 + arr[1]>7*60 and (arr[0]+2)*60 + arr[1]<10*60 or (arr[0]+2)*60 + arr[1]>15*60 and (arr[0]+2)*60 + arr[1]<19*60):
    if((arr[0]+2)*60 + arr[1]>7*60 and (arr[0]+2)*60 + arr[1]<10*60):
        lefttime = (arr[0]+2)*60 + arr[1] - 7*60
        print(lefttime)
        if(lefttime <120):
            ans = (arr[0])*60 + arr[1] + (7*60-(arr[0])*60 + arr[1])+lefttime*2
            
        if(lefttime >= 120):
            nonehalftime = lefttime - 180
            ans =(arr[0])*60 + arr[1] + 120*2 + nonehalftime // 2
            
    if((arr[0]+2)*60 + arr[1]>15*60 and (arr[0]+2)*60 + arr[1]>19*60):
        lefttime = (arr[0]+2)*60 + arr[1] - 15*60
        
        if(lefttime <=120):
            ans = (arr[0])*60 + arr[1] + (15*60-(arr[0])*60 + arr[1])+lefttime*2
            
        if(lefttime > 120):
            nonehalftime = lefttime - 180
            ans =(arr[0])*60 + arr[1] + 120*2 + nonehalftime // 2
            
else :
    ans +=(arr[0]+2)*60 + arr[1]

a = ans%60
b = (ans-ans%60) // 60
if(b>= 24):
    b -= 24
if(b<10):
    b = "0" + str(b)
if(a==0):
    a = "0" + str(a)

print(str (b) + ":" + str(a))
