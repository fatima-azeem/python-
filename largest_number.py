# Taking input from the user 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the second number: "))

# Checking for the largest number 
if num1 >= num2 and num1 >= num3 :
    print(str(num1) + " is the Largest Number ")
elif num2 >= num1 and num2 >= num3 :
    print(str(num2) + " is the Largest Number ")
else:
    print(str(num3) + " is the Largest Number ")