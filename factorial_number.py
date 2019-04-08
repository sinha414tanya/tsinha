num=int(input())

def find_fact(num):
    if num<=20:
        f=1
        for i in range(1,num+1):
            f=f*i
        print(f)
    else:
        print("invalid input")
find_fact(num)

