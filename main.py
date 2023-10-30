import math

print("Инженерный калькулятор")
print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Возведение в степень")
print("6. Квадратный корень")
print("7. Факториал")
print("8. Синус")
print("9. Косинус")
print("10. Тангенс")

operation = input("Введите номер операции: ")


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Ошибка: невозможно деление на 0"


def exponentiation(a, b):
    return a ** b


def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Ошибка: невозможно извлечь квадратный корень из отрицательного числа"


def factorial(a):
    if a >= 0:
        return math.factorial(a)
    else:
        return "Ошибка: невозможно вычислить факториал отрицательного числа"


def sine(a):
    return math.sin(a)


def cosine(a):
    return math.cos(a)


def tangent(a):
    return math.tan(a)


if operation in ['1', '2', '3', '5']:
    number1 = float(input("Вве1дите первое число: "))
    number2 = float(input("Введите второе число: "))
    if operation == '1':
        result = addition(number1, number2)
        print(f"Результат: {result}")
    elif operation == '2':
        result = subtraction(number1, number2)
        print(f"Результат: {result}")
    elif operation == '3':
        result = multiplication(number1, number2)
        print(f"Результат: {result}")
    elif operation == '5':
        result = exponentiation(number1, number2)
        print(f"Результат: {result}")

elif operation in ['4', '6', '7', '8', '9', '10']:
    number = float(input("Введите число: "))
    if operation == '4':
        divisor = float(input("Введите делитель: "))
        result = division(number, divisor)
        print(f"Результат: {result}")
    elif operation == '6':
        result = square_root(number)
        print(f"Результат: {result}")
    elif operation == '7':
        result = factorial(number)
        print(f"Результат: {result}")
    elif operation == '8':
        result = sine(number)
        print(f"Результат: {result}")
    elif operation == '9':
        result = cosine(number)
        print(f"Результат: {result}")
    elif operation == '10':
        result = tangent(number)
        print(f"Результат: {result}")

else:
    print("Ошибка: неверный номер операции")
