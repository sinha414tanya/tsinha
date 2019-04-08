st=str(input())
l=len(st)

def display_reverse(st,l):
    if l<=100000:
        rev=st[::-1]
        print(rev)

display_reverse(st,l)