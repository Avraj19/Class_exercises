from exercise_111 import *

# print(add(6,3))
print('Hello what would you operation would you like to perform with 2 numbers, \n'
      'option: add, subtract, multiply, divide, area of a triangle, area of a circle or area of a square.\n'
      ':')

user_input =input('').strip().lower()
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if user_input == 'add':
    print(add(num1,num2))

elif user_input == 'subtract':
    print(sub(num1,num2))
elif user_input == 'multiply':
    print(mult(num1, num2))

elif user_input == 'divide':
    print(div(num1, num2))

elif user_input == 'area of a triangle':
    print(area_of_triangle(num1, num2))

elif user_input == 'area of a circle':
    print(area_of_circle(num1, num2))

else:
    print('Invalid input')