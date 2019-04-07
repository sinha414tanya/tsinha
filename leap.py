year=int(input())

def check_leap(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                print("yes")
            else:
                print("no")
        else:
            print("yes")
    else:
        print("no")

check_leap(year)

