num=int(input())
def check_pallindrome(num):
    if num<=1000:
        st=str(num)
        st_rev=st[::-1]
        if st==st_rev:
            return True
        else:
            return False
    else:
        return -1
if check_pallindrome(num)==True:
    print("yes")
elif check_pallindrome(num)==False:
    print("no")
else:
    print("invalid input")