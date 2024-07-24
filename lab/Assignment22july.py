# Assignment:
print("22 july  lab Assignment:")
# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
print("This is a Python program to handle a ZeroDivisionError exception when dividing a number by zero")

try:
    print(100/0)
except ZeroDivisionError as e:
    print(e)

print("------------------------------------------------")
# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
print("This is a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer ")
user_input = input("please enter a value ")
try:
        user_input = int(user_input)
        print(f"You entered a valid integer: {user_input}")
except ValueError:
        raise ValueError("Invalid input! Please enter a valid integer.")

print("------------------------------------------------")
# 3. Write a Python program that opens a file and handles a FileNotFoundError exception the file does not exist.
print("This is a Python program that opens a file and handles a FileNotFoundError exception the file does not exist")

try:
      open("text.txt")
except FileNotFoundError:
      print("File not found error ")

print("------------------------------------------------")

# 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical
print("This is a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical")
try:
        num1 = input("Please enter the first number: ")
        num2 = input("Please enter the second number: ")

        # Attempt to convert inputs to float
        num1 = float(num1)
        num2 = float(num2)

        print(f"You entered valid numbers: {num1} and {num2}")

except ValueError:
        raise TypeError("Invalid input! Both inputs must be numerical.")