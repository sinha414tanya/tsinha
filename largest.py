a,b,c=list(map(int,input().split()))

def check(a,b,c):
    if(a>b and a>c):
        print(a)
    else:
        if(b>c):
            print(b)
        else:
            print(c)
check(a,b,c)
