'''
 Find GCD
Send Feedback
You are given two numbers. You need to calculate and print their greatest common divisor (GCD).
Draw a flowchart for this process.
'''
a=int(input())
b=int(input())
i=1
small=min(a,b)
gcd=1
for k in range(i,small+1):
    if a%k==0 and b%k==0:
        gcd=k
print(gcd)
