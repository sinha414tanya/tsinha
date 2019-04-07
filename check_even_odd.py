num=int(input())
def check_even_odd(num):
    if(num<0):
        print("invalid")
    else:
        if(num%2==0):
            print(Even)
        else:
            print("Odd")

check_even_odd(num)