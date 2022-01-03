x=int(input("enter a num"))
sum=1
if x<0:
    print("-ve")
elif (x==0) or (x==1):
    print(x)
else:
    while (x>1):
        sum=sum*x
        x=x-1
    print(sum)