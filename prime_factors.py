n=int(input())
a=[]
for i in range(2,n+1):
    if n%i==0:
        a.append(i)
def check(num):
    c=0

    for i in range(2,num):
        if(num%i==0):
            c=c+1
    if c==0:
        return True
    else:
        return False
b=[]
for i in a:
    if(check(i)==True):
        b.append(i)
print(*b)





