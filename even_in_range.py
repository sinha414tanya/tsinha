p,q=list(map(int,input().split()))

def even_in_range(p,q):
    arr=[]
    if p%2==0:
        for i in range(p+1,q):
            if i%2==0:
                arr.append(i)
    else:
        for i in range(p,q):
            if i%2==0:
                arr.append(i)
    print(*arr)

even_in_range(p,q)