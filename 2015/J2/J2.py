def takeinput():
    x = input()
    happy = x.count(":-)")
    sad = x.count(":-(")
    return happy,sad

def happyorsad(happy,sad):
    if(happy>sad):
        print("happy")
    elif(happy<sad):
        print("sad")
    elif(happy == 0 and sad == 0):
        print("none")
    elif(happy == sad):
        print("unsure")
happy,sad = takeinput()
happyorsad(happy,sad)
