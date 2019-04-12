num1=int(input())

def check_armstrong(num1):
    if num1<=100000:
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
if check_armstrong(num1)==True:
    print("yes")
else:
    print("no")
