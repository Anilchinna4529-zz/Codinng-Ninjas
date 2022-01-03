'''
largest of three 3 numbers
'''
x=int(input("1st num : "))
y=int(input("2nd num : "))
z=int(input("3rd num :"))
if x>y and x>z:
    print("X is greater",x)
elif y>x and y>z:
    print("y is great",y)
else:
    print("z is great",z)