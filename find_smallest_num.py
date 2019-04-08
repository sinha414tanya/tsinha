
l,r=list(map(int,input().split()))
def check(l,r):
    a=[]
    if 1<=l<=100000 and 1<=r<=100000:
        for i in range(1,100000):
            if(i%l==0 and i%r==0):
                a.append(i)
        print(min(a))
    else:
        print("invalid input")
check(l,r)