ch=input()
def check(ch):
    if(ch>="a" and ch<="z") or (ch>="A" and ch<="Z"):
        if ch in 'aeiou' or ch in "AIEOU":
            print("Vowel")
        else:
            print("Consonent")
    else:
        print("invalid")
check(ch)

