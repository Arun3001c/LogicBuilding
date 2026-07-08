#first program

number=int(input("Enter a number: "))
print("square:",number**2,"cube:",number**3)

#second program
radius , base, height = map(int, input("Enter the radius, base and height: ").split())
def area_of_circle(radius):
    return 3.14 * radius * radius
def area_of_triangle(base, height):
    return 0.5 * base * height
print("Area of circle:", area_of_circle(radius))
print("Area of Triangle:", round(area_of_triangle(base, height),0))
# =========================
# FLOAT HANDLING IN PYTHON
# =========================

# 1. int()
# - Removes decimal part (TRUNCATES, does NOT round)
# - Example:
#   int(3.9) → 3
#   int(3.1) → 3
# - Use when you want only whole number part

# 2. round(number, n)
# - Rounds number to n decimal places
# - Example:
#   round(3.14159, 2) → 3.14
#   round(3.6) → 4
# - Use when you want proper mathematical rounding

# 3. f-string formatting (BEST METHOD)
# - Controls display of float values
# - Syntax: f"{number:.nf}"
# - Example:
#   x = 3.14159
#   print(f"{x:.2f}") → 3.14
#   print(f"{x:.3f}") → 3.142
# - Use for clean output formatting

# 4. format() method (older style)
# - Example:
#   "{:.2f}".format(3.14159) → 3.14

# =========================
# QUICK RULE
# =========================
# - int()   → remove decimals
# - round() → proper rounding
# - f-string → best for printing formatted output

#3rd question
dividend, divisor = map(int, input("Enter dividend and divisor: ").split())
quotient = dividend // divisor
remainder = dividend % divisor
print("Quotient:", quotient, "Remainder:", remainder)

