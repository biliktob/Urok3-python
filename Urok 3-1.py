def func1():
    arg1 = int(input("Уважаемый, введите делимое: "))
    arg2 = int(input("Введите делитель: "))
    return arg1 / arg2 if arg2 != 0 else "На ноль делить нельзя"
tex = (func1())
text = (f"частное составляет: {tex}")
print(text)