num=int(input())

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

if check_prime(num)==True:
    print("yes")
elif check_prime(num)==False:
    print("no")
else:
    print("no")