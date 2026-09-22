# 1. Employee Bonus

print("\n--- 1. Employee Bonus ---")

salary = float(input("Enter salary: "))
experience = int(input("Enter years of experience: "))

if experience >= 10:
    bonus = salary * 20 / 100
elif experience >= 5:
    bonus = salary * 10 / 100
elif experience >= 2:
    bonus = salary * 5 / 100
else:
    bonus = 0

total_salary = salary + bonus

print("Bonus amount:", bonus)
print("Total salary:", total_salary)


# 2. ATM Withdrawal System

print("\n--- 2. ATM Withdrawal System ---")

correct_pin = 1234
balance = 50000

pin = int(input("Enter PIN: "))

if pin != correct_pin:
    print("Invalid PIN")
else:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Withdrawal amount must be greater than 0")
    elif amount % 100 != 0:
        print("Amount must be a multiple of 100")
    elif amount > balance:
        print("Insufficient balance")
    else:
        balance = balance - amount
        print("Withdrawal successful")
        print("Remaining balance:", balance)


# 3. Income Tax Calculator

print("\n--- 3. Income Tax Calculator ---")

income = float(input("Enter annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 5 / 100
elif income <= 1000000:
    tax = income * 20 / 100
else:
    tax = income * 30 / 100

remaining_income = income - tax

print("Tax amount:", tax)
print("Remaining income:", remaining_income)


# 4. Shopping Discount System

print("\n--- 4. Shopping Discount System ---")

amount = float(input("Enter purchase amount: "))
member = input("Are you a member? (yes/no): ")

if member == "yes":
    if amount >= 10000:
        discount_percent = 20
    elif amount >= 5000:
        discount_percent = 15
    elif amount >= 2000:
        discount_percent = 10
    else:
        discount_percent = 0
else:
    if amount >= 10000:
        discount_percent = 10
    elif amount >= 5000:
        discount_percent = 5
    else:
        discount_percent = 0

discount_amount = amount * discount_percent / 100
final_amount = amount - discount_amount

print("Original amount:", amount)
print("Discount percentage:", discount_percent)
print("Discount amount:", discount_amount)
print("Final amount:", final_amount)


# 5. Driving License Eligibility

print("\n--- 5. Driving License Eligibility ---")

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible")

    test = input("Have you passed the driving test? (yes/no): ")

    if test == "yes":
        print("License can be issued")
    else:
        print("Pass the driving test first")
else:
    print("Not eligible")


# 6. Login System

print("\n--- 6. Login System ---")

username = input("Enter username: ")
password = input("Enter password: ")

if username != "admin":
    print("Invalid username")
elif password != "Python@123":
    print("Invalid password")
else:
    print("Login successful")


# 7. Temperature Classification

print("\n--- 7. Temperature Classification ---")

temperature = float(input("Enter temperature: "))

if temperature < 0:
    print("Freezing")
elif temperature <= 15:
    print("Very Cold")
elif temperature <= 25:
    print("Cold")
elif temperature <= 35:
    print("Normal")
elif temperature <= 45:
    print("Hot")
else:
    print("Extremely Hot")


# 8. Password Strength

print("\n--- 8. Password Strength ---")

password = input("Enter password: ")

if len(password) < 6:
    print("Weak")
elif len(password) <= 9:
    print("Medium")
else:
    has_letter = False
    has_number = False

    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True

    if has_letter and has_number:
        print("Very Strong")
    else:
        print("Strong")


# 9. Restaurant Bill

print("\n--- 9. Restaurant Bill ---")

bill = float(input("Enter restaurant bill: "))

if bill >= 5000:
    discount_percent = 20
elif bill >= 3000:
    discount_percent = 15
elif bill >= 1000:
    discount_percent = 10
else:
    discount_percent = 0

discount = bill * discount_percent / 100
amount_after_discount = bill - discount

gst = amount_after_discount * 5 / 100
final_bill = amount_after_discount + gst

print("Original bill:", bill)
print("Discount:", discount)
print("Amount after discount:", amount_after_discount)
print("GST:", gst)
print("Final bill:", final_bill)


# 10. E-Commerce Coupon System

print("\n--- 10. E-Commerce Coupon System ---")

order = float(input("Enter order amount: "))
coupon = input("Enter coupon code: ")

if coupon == "SAVE20":
    if order >= 2000:
        discount = order * 20 / 100
    else:
        discount = 0
        print("SAVE20 requires minimum order of ₹2000")

elif coupon == "SAVE10":
    if order >= 1000:
        discount = order * 10 / 100
    else:
        discount = 0
        print("SAVE10 requires minimum order of ₹1000")

elif coupon == "WELCOME":
    if order >= 1500:
        discount = 200
    else:
        discount = 0
        print("WELCOME requires minimum order of ₹1500")

else:
    discount = 0
    print("Invalid coupon")

final_amount = order - discount

print("Order amount:", order)
print("Discount:", discount)
print("Final amount:", final_amount)