#first question solution
entered_number = int(input())
print(f"You entered:{entered_number}")

#second question solution
import sys
print("int:", sys.getsizeof(0))
print("float:", sys.getsizeof(0.0))
print("str:", sys.getsizeof(""))
print("list:", sys.getsizeof([]))
print("tuple:", sys.getsizeof(()))
print("set:", sys.getsizeof(set()))
print("dict:", sys.getsizeof({}))
print("bool:", sys.getsizeof(True))

#3rd solution
num1, num2 = map(int, input("Enter two numbers separated by space: ").split())
print("largest number is:", max(num1, num2))