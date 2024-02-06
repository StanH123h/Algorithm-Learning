def cashing(money):
    result = {50: 0, 25: 0, 10: 0, 5: 0, 1: 0}
    count=0
    while money >= 50:
        money -= 50
        result[50] += 1
        count+=1
    while money >=25:
        money -= 23
        result[25]+=1
        count += 1
    while money >=10:
        money-=10
        result[10]+=1
        count += 1
    while money >= 5:
        money-=5
        result[5]+=1
        count += 1
    while money >=1:
        money-=1
        result[1]+=1
        count += 1
    return str(result)+str(count)
print(cashing(63))


