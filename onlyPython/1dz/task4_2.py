name = input("Введите свое имя: ")
surname = input("Введите свою фамилию: ")
age = input("Введите свой возраст: ")

print("Ваше имя: {name}, Фамилия:  {surname}, Возраст: {age} лет".format(name=name, surname=surname, age=age))
print(f"Ваше имя: {name}, Фамилия:  {surname}, Возраст: {age} лет")
# Вывод: в данном случае f-string гораздо удобнее ;D