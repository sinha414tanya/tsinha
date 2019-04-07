limit=int(input())

def sum(limit):
    sum=0
    if(limit>0):
        for i in range(1,limit+1):
            sum=sum+i
        print(sum)
    else:
        print("invalid")
sum(limit)