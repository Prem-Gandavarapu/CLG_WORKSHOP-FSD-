#name=input("Enter your name:")
#print("name:",name)

def arthematic_operation(a,b):
    print("Addition:", a+b)
    print("Subtraction:", a-b)
    print("Multiplication:", a*b)
    print("Division:", a/b)
    print("Floor Division:", a//b)
    print("Modulus:", a%b)

def relational_operation(a,b):
    print("Greater than:", a>b)
    print("Less than:", a<b)
    print("Equal to:", a==b)
    print("Not equal to:", a!=b)

def logical_operation(a,b):
    print("Logical AND:", a>10 and b>10)
    print("Logical OR:", a>10 or b>10)
    print("Logical NOT:", not(a>10))

def bitwise_operation(a,b):
    print("Bitwise AND:", a&b)
    print("Bitwise OR:", a|b)
    print("Bitwise XOR:", a^b)
    print("Bitwise NOT:", ~a)
    print("Left Shift:", a<<1)
    print("Right Shift:", a>>1)

#a = int(input("Enter first number:"))
#b = int(input("Enter second number:"))
#arthematic_operation(a,b)
#relational_operation(a,b)
#logical_operation(a,b)
#bitwise_operation(a,b)

c = input("Enter a quantity of food:")
print("Quantity of food:", c+c)
d=int(input("Enter a quantity of food:"))
print("Quantity of food:", d+d)
total_cost = d*40
print("Total cost of food:", total_cost)
