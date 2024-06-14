# Taking input from the user 
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

# printing the values before swapping 
print("Before swapping: x = " + str(x) + "\n y = " + str(y))
      
# swapping the values
x, y = y, x
      
# printing the values after swapping
print("After swapping: x = " + str(x) + "\n y = " + str(y))  