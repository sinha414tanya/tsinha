num=int(input())
arr=[]
def multiples(num):
    for i in range(1,6):
        m=num*i
        arr.append(m)

    print(*arr)
multiples(num)