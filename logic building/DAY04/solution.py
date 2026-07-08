#first solution 
number=int(input("enter a number: "))
for i in range(1,11):
    print(f"{number} * {i} ={number*i}")
#second solution

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

def calculator():
    print("Welcome to the Simple Calculator!")

    try:
        first_number = float(input("Enter the first number: "))
        operator=input("enter the operator (+, -, *, /): ")
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    #  match operator:
    #     case '+':
    #         result = add(first_number, second_number)
    #     case '-':
    #         result = subtract(first_number, second_number)
    #     case '*':
    #         result = multiply(first_number, second_number)
    #     case '/':
    #         result = divide(first_number, second_number)
    #     case _:
    #         print("Invalid operator. Please use +, -, *, or /.")
    #         return
    if operator == '+':
        result = add(first_number, second_number)
    elif operator == '-':
        result = subtract(first_number, second_number)  
    elif operator == '*':
        result = multiply(first_number, second_number)
    elif operator == '/':
        if second_number == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = divide(first_number, second_number)
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return
    print(f"{first_number} {operator} {second_number} = {result}")
calculator()

#3rd solution
# def reverse_number_string(num):
#     # Convert the number to a string
#     num_str = str(num)

#     # Reverse the string using slicing
#     reversed_str = num_str[::-1]

#     # Convert back to an integer (optional)
#     reversed_num = int(reversed_str)

#     return reversed_num
# number = int(input("Enter a number to reverse: "))
# reversed_number = reverse_number_string(number)
# print(f"The reverse of {number} is {reversed_number}")
number=int(input("enter a number: "))
temp=number
reverse_number=0
while temp>0:
    remainder=temp%10
    reverse_number=(reverse_number*10)+remainder
    temp=temp//10
print("reversed number is ", reverse_number)