def func2():
    name = str(input("Уважаемый, введите имя: "))
    surname = str(input("Введите фамилию: "))
    birth_year = str(input("Введите год рождения: "))
    email = str(input("Введите электронную почту: "))
    phone = str(input("Введите номер телефона: "))
    return (f"Имя: {name}, фамилия: {surname}, год рождения: {birth_year}, электронная почта: {email}, номер телефона: {phone}")
print(func2())