def is_num(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


while True:
    x = input("Введите число: ")
    
    if is_num(x) == True:
        print("Длина введенного числа: " + str(len(x)))
        continue
    else:
        if x == 'exit':
            break 
        else:
            print("Вы ввели не число")
            continue