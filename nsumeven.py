x=int(input())
sum=0
#sum2=0
if x%2==0:
    for i in range(1,x-1):
        if i%2==0:
            sum=sum+i

else:
    for i in range(1,x-1):
        if i%2!=0:
            sum=sum+1
print(sum)