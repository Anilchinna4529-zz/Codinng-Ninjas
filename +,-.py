'''' Check Number
Send Feedback
You are given a single number. You need to print one of the following outputs according to the number's nature.
Print 1, if the number is positive
Print -1, if it's negative
Print 0, if it's equal to 0
Draw a flowchart for this process.
'''
x=int(input("enter the number"))
if x>0:
    print("it is postive num ",x)
elif x<0:
    print("it is - ",x)
elif x==0:
    print("zero",x)
else:
    exit
    