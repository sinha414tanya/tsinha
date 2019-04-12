num1,num2=list(map(int,input().split()))
arr=[]

def check_prime(num):
    if num<=1000:
        if num==2:
            return True
        elif num<=1:
            return False
        else:
            c=0
            for i in range(2,num):
                if(num%i==0):
                    c=c+1

            if c==0:
                return True
            else:
                return False

    else:
        return -1
if num1%2==0:
    for i in range(num1+1,num2):
        if check_prime(i)==True:
            arr.append(i)
else:
    for i in range(num1,num2):
        if check_prime(i)==True:
            arr.append(i)
print(*arr)
