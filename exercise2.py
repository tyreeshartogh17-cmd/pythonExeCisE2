# ====================================================================================
# Question 1: Arithmetic and Assignment Operators
# ====================================================================================
# (Example initial values provided for testing purposes)
x = 5
y = 4

# TODO: Add 3 to x using the += operator
x += 3

# TODO: Multiply y by 2 using the *= operator
y *= 2

# TODO: Divide x by y and store the result in a variable called 'result'
result = x / y

# TODO: Print the value of 'result'
print("Result of Question 1:", result)


#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators
#------------------------------------------------------------------------------------
# (Example initial values provided for testing purposes)
a = 10
b = 6
c = 8

# TODO: Create a condition that checks if a is greater than b
cond1 = a > b

# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
cond2 = b % 2 == 0

# TODO: Create a condition that checks if c is less than or equal to a
cond3 = c <= a

# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
final_condition = cond1 or (cond2 and cond3)

# TODO: Print the value of 'final_condition'
print("Final Condition of Question 2:", final_condition)


#------------------------------------------------------------------------------------
# Question 3: Conditional Statements
#------------------------------------------------------------------------------------

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = float(input("Enter a test score (0-100): "))

# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
else:
    grade = "F"

# TODO: Print the grade for the given score
print("Your grade is:", grade)


#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals
#------------------------------------------------------------------------------------

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("Enter an operation (+, -, *, /): ")

# TODO: Use conditional statements to perform the chosen operation on num1 and num2
# TODO: Handle the case of division by zero
calc_result = None

if operation == "+":
    calc_result = num1 + num2
elif operation == "-":
    calc_result = num1 - num2
elif operation == "*":
    calc_result = num1 * num2
elif operation == "/":
    if num2 == 0:
        calc_result = "Error: Division by zero is not allowed."
    else:
        calc_result = num1 / num2
else:
    calc_result = "Error: Invalid operation selected."

# TODO: Print the result of the operation
print("Operation result:", calc_result)
