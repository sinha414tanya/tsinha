num1=int(input())

def sum(num1):
    s=0
    if 1<=num1<=1000000000000000000:
        while(num1!=0):
            c=num1%10
            sq=c*c
            s=s+sq
            num1=int(num1/10)
        print(s)
    else:
        print("invalid input")


sum(num1)