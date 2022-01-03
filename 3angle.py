#check Triangle
x=int(input())
y=int(input())
z=int(input())
if x==y==z:
    print("it is a equilateral triangle")
elif x==y or y==z:
    print("it is a isosceles triangle")
else:
    print("It is a Scalene triangle")
