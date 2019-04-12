num1,num2=list(map(int,input().split()))
arr=[]
def check_armstrong(num1):
    num = num1
    st=str(num1)
    l=len(st)
    sum=0
    while(num>0):
        c=num%10
        sum=sum+(c**l)
        num=num//10
    if int(num1)==sum:
        return True
    else:
        return False

for i in range(num1,num2):
    if check_armstrong(i)==True:
        arr.append(i)
print(*arr)