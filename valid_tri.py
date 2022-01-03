'''
 Valid Triangle
Send Feedback
You are given 3 numbers. Each number represents the length of a line. You need to figure out whether these lines can form a valid triangle.
If a valid triangle can be formed, print "Yes", otherwise print "No".
Draw a flowchart for this process
A triangle is a valid triangle, If and only If, the sum of any two sides of a triangle is greater than the third side. For Example, let A, B and C are three sides of a triangle. Then, A + B > C, B + C > A and C + A > B
'''
a=int(input("enter the 1st angle of a tringle: "))
b=int(input("enter the 2rd angle of tringle: "))
c=int(input("enter the 3rd angle of triangle: "))
if a+b>c and b+c>a and c+a>b:
    print("valid triangle")
else:
    print("not valid tringle")