x = int(input("Введите число(пожалуйста, тут нет проверки на тип): "))
neg_sum = 0
pos_sum = 0

for i in range(-x, x+1):
    print("Число: ", i)
    
    if i < 0:
        neg_sum += i
        
    else:
        pos_sum += i
        
print("Сумма положительных чисел: ", pos_sum)
print("Сумма отрицательных чисел: ", neg_sum)
