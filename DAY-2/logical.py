a=int(input("Enter a Marks of subject1:"))
b=int(input("Enter a Marks of subject2:"))
c=int(input("Enter a Marks of subject3:"))
if a>=35 and b>=35 and c>=35:
    print("You are pass")
elif a>=35 or b>=35 or c>=35:
    print("You are pass in one subject")
else:
    print("You are fail")