num = int(input("Enter a number whose multiples you want: "))
l = int(input("Enter the lower limit: "))
u = int(input("Enter the upper limit: "))

for x in range(l, u + 1, 1):
  if x % num == 0:
    print(x)