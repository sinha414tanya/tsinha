st=str(input())
def conver_into_camel(st):
    if len(st)<=1000000:
        print(st.title())
    else:
        print("invalid input")
conver_into_camel(st)