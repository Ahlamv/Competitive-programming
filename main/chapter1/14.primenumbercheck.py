def prime(num):
    boolisprime=True
    i=2
    while i<=num/2:
        if num%i==0:
            isprime=False
        i+=1
    if(isprime):
        print("Prime number")
    else:
        print("Not prime number")

prime(6)