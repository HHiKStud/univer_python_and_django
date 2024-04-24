dct = {1: 11,
       2: 22,
       3: 33,
       4: 4,
       5: 33,  # при создании множества значений это пропадет, т.к дубликат
       6: 1}

set_keys = set()
#set_keys = set(dct)  # ключи проще достать так 
set_values: set = set()
set_united: set = set()

for k, v in dct.items():
    set_keys.add(k)
    set_values.add(v)

set_united = set_keys | set_values  # ну или через union()

print(set_keys)
print(set_values)
print(set_united)
# Вывод: при объединении множеств удалились одинаковые значения