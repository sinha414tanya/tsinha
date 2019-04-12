num=int(input())

def find_factorial(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    print(f)

find_factorial(num)