N=int(input())
array=list(map(int,input().split()))

def display_min(N,array):
    if(1<=N<=100000):
        array.sort()
        print(array[0])


display_min(N,array)
