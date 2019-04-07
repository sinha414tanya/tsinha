n=int(input())
array=list(map(int,input().split()))
def median(n,array):
    if(1<=n<=1000):
        array.sort()
        a=int(n/2)
        print(array[a])
median(n,array)
