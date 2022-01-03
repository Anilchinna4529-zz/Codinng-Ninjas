'''
Check prime number or not
'''
n=int(input("num"))
div=2
while div<n:
    if n%div==0:
        print("not prime")
        break
    div=div+1
else:
    print("prime")
