# take user input for name and print
# name = input("Enter your name:- ")
# print("Your name is: ",name)

# 2. Take 2 numbers and print(sum, difference,product,division)
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# sum = num1 + num2
# print(sum)
# print(type(sum))
# print(num1-num2)
# print(num1*num2)
# print(type(num1/num2))

# Take a number and print its square and cube
# num = int(input("Enter a number: "))
# square = num**2
# print("Square of the number is: ",square)
# cube = pow(num, 3)
# print("Cube of the number is: ", cube)


# Take 3 numbers and print their average
# num1 = int(input("First number: "))
# num2 = int(input("Second number: "))
# num3 = int(input("Third number: "))

# average = (num1+num2+num3)/3
# print("The average of the number is ",average)

# print("Hello World")
# print("I am here to conqure.")

num = int(input("Enter a number: "))

# Handle negative numbers by stripping the sign, reversing, and reapplying
if num < 0:
    reversed_num = -int(str(num)[1:][::-1])
else:
    reversed_num = int(str(num)[::-1])

print("Reversed Number:", reversed_num) 