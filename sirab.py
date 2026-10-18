# Task 1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Numbers are equal")


# Task 2
n = float(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


# Task 3
n = int(input("Enter an integer: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


# Task 4
score = int(input("Enter score: "))

if score < 0:
    print("Invalid score")
elif score > 100:
    print("Invalid score")
elif score > 90:
    print("Grade: A")
elif score > 80:
    print("Grade: B")
elif score > 70:
    print("Grade: C")
elif score > 60:
    print("Grade: D")
elif score > 50:
    print("Grade: E")
else:
    print("Grade: F")


# Task 5
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a > b:
    if a > c:
        print("Largest is", a)
    else:
        print("Largest is", c)
else:
    if b > c:
        print("Largest is", b)
    else:
        print("Largest is", c)


# Task 6
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /, %, **, //): ")

match op:
    case "+":
        print("Result:", a + b)
    case "-":
        print("Result:", a - b)
    case "*":
        print("Result:", a * b)
    case "/":
        if b == 0:
            print("Error: second number cannot be zero")
        else:
            print("Result:", a / b)
    case "%":
        if b == 0:
            print("Error: second number cannot be zero")
        else:
            print("Result:", a % b)
    case "**":
        if a == 0 and b < 0:
            print("Error: zero cannot be raised to a negative power")
        elif a < 0 and b != int(b):
            print("Error: negative number cannot be raised to a non-integer power")
        else:
            print("Result:", a ** b)
    case "//":
        if b == 0:
            print("Error: second number cannot be zero")
        else:
            print("Result:", a // b)
    case _:
        print("Invalid operation")


# Task 7
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age <= 12:
    print("Child")
elif age <= 17:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")


# Task 8
amount = float(input("Enter purchase amount (AZN): "))

if amount < 0:
    print("Invalid amount")
else:
    if amount < 100:
        percent = 0
    elif amount < 300:
        percent = 10
    elif amount < 500:
        percent = 15
    else:
        percent = 20

    discount = amount * percent / 100
    final = amount - discount

    print(f"Original price: {amount:.2f} AZN")
    print(f"Discount: {discount:.2f} AZN")
    print(f"Final price: {final:.2f} AZN")


# Task 9
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    t = a
    a = b
    b = t
if b > c:
    t = b
    b = c
    c = t
if a > b:
    t = a
    a = b
    b = t

print(a, b, c)


# Task 10
balance = 1000
amount = float(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient balance")
else:
    balance = balance - amount
    print("Remaining balance:", balance, "AZN")


# Task 11
usage = float(input("Enter usage (kWh): "))

if usage < 0:
    print("Invalid usage")
else:
    if usage <= 100:
        rate = 0.08
    elif usage <= 300:
        rate = 0.12
    else:
        rate = 0.15

    bill = usage * rate

    print("Usage:", usage, "kWh")
    print("Rate:", rate, "AZN/kWh")
    print(f"Total bill: {bill:.2f} AZN")


# Task 12
km = float(input("Enter distance (km): "))

if km < 0:
    print("Invalid distance")
else:
    start_fee = 2

    if km <= 5:
        rate = 0.70
    elif km <= 15:
        rate = 0.60
    else:
        rate = 0.50

    distance_fee = km * rate
    total = start_fee + distance_fee

    print(f"Starting fee: {start_fee:.2f} AZN")
    print(f"Distance fee: {distance_fee:.2f} AZN")
    print(f"Total fare: {total:.2f} AZN")


# Task 13
age = int(input("Enter age: "))
salary = int(input("Enter monthly salary (AZN): "))
loan = int(input("Enter requested loan amount (AZN): "))

if age < 0:
    print("Invalid input: age cannot be negative")
elif salary < 0:
    print("Invalid input: salary cannot be negative")
elif loan <= 0:
    print("Invalid input: loan amount must be more than 0")
else:
    if age < 18:
        print("Decision: Rejected")
        print("Reason: age is below 18")
    elif salary < 500:
        print("Decision: Rejected")
        print("Reason: salary is below 500 AZN")
    elif loan > 10 * salary:
        print("Decision: Rejected")
        print("Reason: loan is more than 10 times the salary")
    else:
        print("Decision: Approved")
        print("Reason: all checks passed")


# Task 14
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a <= 0:
    print("Triangle cannot be created")
elif b <= 0:
    print("Triangle cannot be created")
elif c <= 0:
    print("Triangle cannot be created")
else:
    if a + b > c:
        if a + c > b:
            if b + c > a:
                if a == b:
                    if b == c:
                        print("Equilateral")
                    else:
                        print("Isosceles")
                elif a == c:
                    print("Isosceles")
                elif b == c:
                    print("Isosceles")
                else:
                    print("Scalene")
            else:
                print("Triangle cannot be created")
        else:
            print("Triangle cannot be created")
    else:
        print("Triangle cannot be created")


# Task 15
exam = int(input("Enter exam score (0-700): "))
school = int(input("Enter school score (0-100): "))
age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
elif exam < 0:
    print("Invalid exam score")
elif exam > 700:
    print("Invalid exam score")
elif school < 0:
    print("Invalid school score")
elif school > 100:
    print("Invalid school score")
elif age < 16:
    print("Result: Rejected")
    print("Reason: applicant is younger than 16")
elif exam >= 600:
    print("Result: Scholarship")
    print("Reason: exam score is 600 or higher")
elif exam >= 450:
    print("Result: Accepted")
    print("Reason: exam score is between 450 and 599")
elif exam >= 300:
    if school >= 80:
        print("Result: Accepted")
        print("Reason: exam score is 300-449 and school score is at least 80")
    else:
        print("Result: Rejected")
        print("Reason: exam score is 300-449 but school score is below 80")
else:
    print("Result: Rejected")
    print("Reason: exam score is below 300")


# Task 16
score = int(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")
else:
    result = "Pass" if score >= 51 else "Fail"
    print(result)


# Task 17
total = float(input("Enter order total (AZN): "))
member = input("Are you a member? (yes/no): ")

if total < 0:
    print("Invalid total")
elif member != "yes" and member != "no":
    print("Invalid answer")
else:
    fee = 0 if (total >= 50 or member == "yes") else 5
    final = total + fee

    print(f"Delivery fee: {fee:.2f} AZN")
    print(f"Final total: {final:.2f} AZN")


# Task 18
day = int(input("Enter day number (1-7): "))

match day:
    case 1:
        print("Monday")
        print("Study day")
    case 2:
        print("Tuesday")
        print("Study day")
    case 3:
        print("Wednesday")
        print("Study day")
    case 4:
        print("Thursday")
        print("Study day")
    case 5:
        print("Friday")
        print("Study day")
    case 6:
        print("Saturday")
        print("Weekend")
    case 7:
        print("Sunday")
        print("Weekend")
    case _:
        print("Invalid day")


# Task 19
code = input("Enter drink code (T = Tea, C = Coffee, J = Juice): ")
quantity = int(input("Enter quantity (1-10): "))

match code:
    case "T":
        drink = "Tea"
        price = 2
    case "C":
        drink = "Coffee"
        price = 4
    case "J":
        drink = "Juice"
        price = 3
    case _:
        drink = "Unknown"
        price = 0

if price == 0:
    print("Unknown drink code")
elif quantity < 1 or quantity > 10:
    print("Invalid quantity")
else:
    total = price * quantity
    order_type = "Large order" if total >= 20 else "Regular order"

    print("Drink:", drink)
    print("Quantity:", quantity)
    print("Total:", total, "AZN")
    print(order_type)


# Task 20
student_id = input("Enter student ID: ")

if len(student_id) == 0:
    print("Student ID is required")
elif len(student_id) != 8:
    print("Student ID must have exactly 8 digits")
elif not student_id.isascii() or not student_id.isdecimal():
    print("Student ID must contain digits 0-9 only")
else:
    print("Student ID accepted")


# Task 21
stored_pin = "0427"
pin = input("Enter PIN: ")

if len(pin) == 0:
    print("PIN is required")
elif len(pin) != 4:
    print("PIN must have 4 digits")
elif not pin.isascii() or not pin.isdecimal():
    print("Digits only")
elif pin == stored_pin:
    print("Access granted")
else:
    print("Incorrect PIN")


# Task 22
phone = input("Enter phone number (0XXXXXXXXX): ")

if len(phone) == 0:
    print("Phone number is required")
elif len(phone) != 10:
    print("Phone number must have exactly 10 digits")
elif not phone.isascii() or not phone.isdecimal():
    print("Digits only")
elif phone[0] != "0":
    print("Phone number must start with 0")
else:
    prefix = phone[0:3]

    match prefix:
        case "050" | "051" | "055" | "070" | "077" | "099":
            print("Phone number accepted")
        case _:
            print("Invalid prefix")


# Task 23
balance = 1000
stored_pin = "0427"

pin = input("Enter PIN: ")
amount_text = input("Enter amount to withdraw: ")

if len(pin) != 4 or not pin.isascii() or not pin.isdecimal():
    print("Invalid PIN format: PIN must be exactly 4 digits")
elif pin != stored_pin:
    print("Incorrect PIN")
elif len(amount_text) == 0:
    print("Amount is required")
elif not amount_text.isascii() or not amount_text.isdecimal():
    print("Amount must contain digits only")
else:
    amount = int(amount_text)

    if amount < 10 or amount > 500:
        print("Amount must be between 10 and 500 AZN")
    elif amount % 10 != 0:
        print("Amount must be divisible by 10")
    else:
        fee = 0 if amount <= 200 else 2

        if amount + fee > balance:
            print("Insufficient balance")
        else:
            balance = balance - amount - fee
            print("Withdrawal amount:", amount, "AZN")
            print("Fee:", fee, "AZN")
            print("New balance:", balance, "AZN")


# Task 24
product = input("Enter product code (K, M, H): ")
quantity_text = input("Enter quantity (1-5): ")
coupon = input("Enter coupon code (NONE or SAVE10): ")
delivery = input("Enter delivery code (P = Pickup, S = Standard): ")

match product:
    case "K":
        name = "Keyboard"
        price = 40
    case "M":
        name = "Mouse"
        price = 20
    case "H":
        name = "Headphones"
        price = 60
    case _:
        name = "Unknown"
        price = 0

if price == 0:
    print("Invalid product code")
elif len(quantity_text) == 0:
    print("Quantity is required")
elif not quantity_text.isascii() or not quantity_text.isdecimal():
    print("Quantity must contain digits only")
else:
    quantity = int(quantity_text)

    if quantity < 1 or quantity > 5:
        print("Quantity must be from 1 to 5")
    elif coupon != "NONE" and coupon != "SAVE10":
        print("Invalid coupon code")
    else:
        subtotal = price * quantity

        if coupon == "SAVE10" and subtotal < 100:
            print("Coupon SAVE10 is not eligible (subtotal is below 100 AZN)")
        else:
            if coupon == "SAVE10":
                discount = subtotal * 10 / 100
            else:
                discount = 0

            discounted = subtotal - discount

            match delivery:
                case "P":
                    delivery_fee = 0
                    delivery_ok = True
                case "S":
                    delivery_fee = 0 if discounted >= 80 else 5
                    delivery_ok = True
                case _:
                    delivery_ok = False
                    print("Invalid delivery code")

            if delivery_ok == True:
                final_total = discounted + delivery_fee

                print("Product:", name)
                print("Quantity:", quantity)
                print(f"Subtotal: {subtotal:.2f} AZN")
                print(f"Discount: {discount:.2f} AZN")
                print(f"Delivery fee: {delivery_fee:.2f} AZN")
                print(f"Final total: {final_total:.2f} AZN")
