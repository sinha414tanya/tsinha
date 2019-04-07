num=input()
def check(num):
    if num.isdigit():
        if(num>=0):
            print("yes")
    elif num.count(".")==1:
        if(num.replace(".","").isdigit()):
            print("yes")
        else:
            print("No")
    else:
        print("No")

check(num)