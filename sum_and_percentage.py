# Taking input from the user 
num1 = int(input("Enter the first subject: "))
num2 = int(input("Enter the second subject: "))
num3 = int(input("Enter the second subject: "))
num4 = int(input("Enter the forth subject: "))
num5 = int(input("Enter the fifth subject: "))

# calculating the sum and percentage
sum = num1 + num2 + num3 + num4 + num5
percentage = (sum / 500) * 100

# printing the sum and percentage
print("The sum of the five subjects is: " + str(sum))
print("The percentage of the five subjects is: " + str(percentage))