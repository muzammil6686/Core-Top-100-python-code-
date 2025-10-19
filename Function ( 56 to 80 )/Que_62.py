def tasbeeh():
    list = []
    for i in range(1, 8):
        tasbeeh = int(input("Enter tasbeeh: "))
        list.append(tasbeeh)
    total = sum(list)   
    print("Total tasbeeh:", total)


tasbeeh()