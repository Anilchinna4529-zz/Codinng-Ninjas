#check Triangle
'''
 Check triangle
Send Feedback
You are given the lengths of 3 sides of a valid triangle. You need to print any one of the following outputs depending on the triangle's nature.
Print 1, if the triangle is equilateral
Print 0, if it's isosceles
Print -1, if it's scalene
Draw a flowchart for this process.
'''
x=int(input())
y=int(input())
z=int(input())
if x==y==z:
    print("it is a equilateral triangle")
elif x==y or y==z:
    print("it is a isosceles triangle")
else:
    print("It is a Scalene triangle")
