# Задача
# Дан список numbers = [1, 2, 15, 3]
# Хочу: список их квадратов
numbers = [1, 2, 15, 3]
squares = []
for number in numbers:
    squares.append(number ** 2)

assert squares == [1, 4, 15 ** 2, 9]

# Короткое решение
squares_2 = [number ** 2 for number in numbers]
assert squares_2 == [1, 4, 15 ** 2, 9]

# Comparing with if
correct_password = "123456"
passwd = input("Enter password")
if passwd == correct_password:
    print("Access granted")
    print("Okay")
else:
    print("Access denied")

print("The end")

# Type boolean
print(passwd == correct_password)
print(type(True))
print(5 > 7)
print("6512".isdigit())
print("-6512".isdigit())

# if elif else
x = int(input("Enter number"))
if x > 1000:
    print("x is large")
elif x > 100:
    print("x is not so large")
else:
    print("x is small")

x = int(input("Enter large even number"))
if x > 1000:
    if x % 2 == 0:
        print("Okay")
    else:
        print("x is not even")
else:
    print("x is not large")

x = int(input("Enter large even number"))
if x > 1000 and x % 2 == 0:
    print("okay")
else:
    print("not okay")

print(True and True)
print(True and False)
print(True or False)
print(not False)

print((1 > 2) and (1 / 0 < 7))
# error
# print((1 / 0 < 7) and (1 > 2))

# comparing decimal numbers
print(0.1 + 0.2 == 0.3)
print(0.1 + 0.2)

from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
print(Decimal(0.1))

# Обыкновеные дроби
from fractions import Fraction

print(Fraction(1, 2) + Fraction(1, 3))

# while loop
correct_password = "12345"
password = input("Enter password")
while password != correct_password:
    print("Incorrect password, try again")
    password = input("Enter password")
print("Access granted")

correct_password = "12345"
password = input("Enter password")
while True:
    password = input("Enter password")
    if password == correct_password:
        break
    print("Incorrect password, try  again")

print("Access granted")

# ax^2 + bx + c = 0
from math import sqrt


# defining function
def quadratic_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    sqrt_d = sqrt(d)
    x1 = (-b + sqrt_d) / (2 * a)
    x2 = (-b - sqrt_d) / (2 * a)
    return x1, x2


print(quadratic_roots(1, -5, 6))


def plus_1(some_number):
    return some_number + 1


print(plus_1(4))

# local and global variables
x = 12
y = 75


def foo(x):
    y = x ** 2
    return y


print(foo(1))
print("x = ", x)
print("y = ", y)

y = 14


def bar(x):
    return x + y


print(bar(7))
y = 98
print(bar(7))


# change global variable into function
def change_x():
    global x
    x = x + 1


x = 5
change_x()
print(x)
change_x()
print(x)


# default function argument
def hello(last_name, first_name, title="Dr."):
    print("Hello, ", title, first_name, last_name)


hello("Potter", "Harry", "Mr.")
hello("Potter", "Harry")
hello(first_name="Harry", last_name="Potter")

x = 1287687.
y = 1287687.
print(x is y)


# функции всегда переопределяется по названию
def foo(x, y=None):
    if y is not None:
        return x * y


foo(4)
foo(4, 2)
