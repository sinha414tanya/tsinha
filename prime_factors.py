n=int(input())
def check(num):
    c=0

    for i in range(2,num):
        if(num%i==0):
            c=c+1
    if c==0:
        return True
    else:
        return False
if 2<=n<=100000:
    a=[]
    b=[]
    for i in range(2,n+1):
        if n%i==0:
            a.append(i)
    for i in a:
        if (check(i) == True):
            b.append(i)
    print(*b)
else:
    print("invalid input")









