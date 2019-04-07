n=int(input())
array=list(map(int,input().split()))
def display(n,array):
    pos=0
    for i in range(0,n):
        print(array[i],end=" ")
        print(pos)
        pos = pos + 1

display(n,array)