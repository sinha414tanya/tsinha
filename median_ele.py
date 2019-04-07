n=int(input())
array=list(map(int,input().split()))
def median(n,array):
    if(1<=n<=1000):
        array.sort()
        if(n%2==0):
            a=int(n/2)
            print(array[a-1])
        else:
            a=int(n/2)
            print(array[a])

median(n,array)
