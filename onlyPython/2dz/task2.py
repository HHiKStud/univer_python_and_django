liters = {}

usr_str = input("Введите любую строчку: ")
usr_str = usr_str.lower()
usr_str = usr_str.replace(" ", "")

for i in usr_str:
    liters[i] = liters.get(i, 0)+1

for k, v in liters.items():
    print(f"Символ \"{k}\" встречается {v} раз")