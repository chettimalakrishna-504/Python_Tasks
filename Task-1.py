# Positive, Negative or Zero *
# Take a number from the user and check whether it is positive, negative, or zero

n = int(input("Enter a number: "))
if n>0:
    print("The number is positive.")
elif n<0:  
    print("The number is negative.")
else:
    print("The number is zero.")


# Largest of Two Numbers
# Take two numbers from the user and find which number is larger. If both are equal, display an appropriate message.

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))   
if n1>n2:
    print(f"{n1} is larger than {n2}.") 
elif n1<n2:
    print(f"{n2} is larger than {n1}.")


# Divisible by 5
# Take a number from the user and check whether it is divisible by 5 or not.

n=int(input("Enter a number: "))
if(n%5==0):
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5")


# Simple Login System
# Ask the user to enter a username and password. Check whether the entered username and password are correct and display the appropriate message.

username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "user" and password == "abc@123":
    print("Login successful!")
else: 
    print("Invalid username or password. Please try again.")


# Triangle Type
# Take three sides of a triangle and determine whether the triangle is Equilateral, Isosceles, or Scalene.

n1 = int(input("Enter the first side of the triangle: "))
n2 = int(input("Enter the second side of the triangle: "))
n3 = int(input("Enter the third side of the triangle: "))
if n1==n2==n3:
    print("The triangle is Equilateral.")
elif n1==n2 or n2==n3 or n1==n3:
    print("The triangle is Isosceles.")
else:
    print("The triangle is Scalene.")