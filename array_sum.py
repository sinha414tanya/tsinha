N,K=list(map(int,input().split()))
array=[]
array=list(map(int,input().split()))

def sum(array,N,K):
    sum=0
    if(K<=N):
        for i in range(0,K):
            sum=sum+array[i]
        print(sum)

sum(array,N,K)