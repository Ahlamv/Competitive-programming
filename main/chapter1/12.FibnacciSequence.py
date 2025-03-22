def fib(num):
    a,b=0,1
    seq=[]
    for i in range(num):
         seq.append(a)
         a,b=b,a+b    
    return seq
print(fib(5))