str=input()
length=len(str)
str=list(str)
for i in range(length):
    str[i]=str[length]
print(str)