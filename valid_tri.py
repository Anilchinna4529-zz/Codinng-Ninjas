a=int(input("enter the 1st angle of a tringle: "))
b=int(input("enter the 2rd angle of tringle: "))
c=int(input("enter the 3rd angle of triangle: "))
if a+b>c and b+c>a and c+a>b:
    print("valid triangle")
else:
    print("not valid tringle")