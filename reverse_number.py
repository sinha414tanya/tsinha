num=input()

def rev(num):
    if num.isdigit():
        st=str(num)
        rev=st[::-1]
        print(rev)
    else:
        print("invalid input")
rev(num)