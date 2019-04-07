N=int(input())
array=list(map(int,input().split()))

def display_sum(N,array):
    if(1>=N<=100000):
        array.sort(reverse=True)
        print(array[0])

display_sum(N,array)
