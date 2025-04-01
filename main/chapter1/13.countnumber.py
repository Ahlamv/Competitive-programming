def count(num):
    i=0
    while num>0:
        i+=1
        num=num//10
    return i
print(count(4000))
