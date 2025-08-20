# You are given 3 integer angles(in degrees), A, B, and C, of a triangle. You have to tell whether the triangle is valid or not. A triangle is valid if the sum of its angles equals 180
A=int(input("Enter A angle="))
B=int(input("Enter B angle="))
C=int(input("Enter C angle="))
if(A+B+C==180):
    print("Hence sum is 180 it Triangle")
else:
    print("Hence sum is not 180 so it is not triangle")