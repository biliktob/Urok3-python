def func3():
    num1 = int(input("Уважаемый, введите первое число: "))
    num2 = int(input("Введите второе число: "))
    num3 = int(input("Введите третье число: "))
    return sum(sorted([num1, num2, num3], reverse=True)[:2])
print(func3())