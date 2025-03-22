def prime(num):
    if num==1 or num==2:
        print("prime")
    elif (num%2==0) or (num%3==0) or (num%5==0):
        print("Not prime")
    else:
        print("prime")
prime(1)