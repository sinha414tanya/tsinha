N=int(input())
array=list(map(int,input().split()))
def sort_array(N,array):
    if 1<=N<=1000:
        array.sort()
        print(*array)


sort_array(N,array)
