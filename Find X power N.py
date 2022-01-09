'''
 Find X raised to power N
Send Feedback
You are given two integers: X and N. You have to calculate X raised to power N and print it.
'''
# Write your code here
n=10
x=4
sum=0
if n>=1 and n<=10:
    if x>=1 and x<=100:
        sum=n**x
print(sum)