p,q=list(map(int,input().split()))

def display_odd(p,q):
    arr=[]
    if p<=100000 and q<=100000:
        if p%2!=0:
            for i in range(p+1,q):
                if i%2!=0:
                    arr.append(i)
        else:
            for i in range(p,q):
                if i%2!=0:
                    arr.append(i)
    print(*arr)

display_odd(p,q)


