
# Getting user inputs for two numbers
num1 = float(input("Type the first number: "))  # Stores the first number in the operation
num2 = float(input("Type the second number: "))  # Stores the second number in the operation

# Storing inputs in a list
input_list = [num1, num2]

# Storing inputs in a dictionary
input_dict = {'first_number': num1, 'second_number': num2}

# Calculating all possible operations
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2 if num2 != 0 else "undefined (division by zero)"

# Storing all calculations in a list
calc_list = [sum_result, difference_result, product_result, quotient_result]

# Storing all calculations in a dictionary
calc_dict = {
    'sum': sum_result,
    'difference': difference_result,
    'product': product_result,
    'quotient': quotient_result
}

# Getting user's choice of operation
operation = input("What type of operation you want me to solve (+, -, *, /): ")  # Inputs the operation choice

# Matching operation and calculating selected result
match operation:
    case "+":
        res = num1 + num2  # Stores the result in an operation of addition
    case "-":
        res = num1 - num2  # Stores the result in an operation of subtraction
    case "*":
        res = num1 * num2  # Stores the result in an operation of multiplication
    case "/":  # Stores the result in an operation of division
        if num2 != 0:  # Denies the division by 0
            res = num1 / num2
        else:
            print("Error: Division by zero!")
            sys.exit(1)
    case _:
        print("Error: Invalid operation! Please use +, -, *, or /")
        sys.exit(1)

# Printing all results
print(f"\nInput List: {input_list}")
print(f"Input Dictionary: {input_dict}")
print(f"All Calculations List: {calc_list}")
print(f"All Calculations Dictionary: {calc_dict}")
print(f"The result of selected operation ({operation}) is equal to {res}")

