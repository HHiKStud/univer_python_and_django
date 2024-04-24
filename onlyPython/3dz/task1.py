def is_num(elem):
        try:
            float(elem)
            return True
        except ValueError:
            return False


while True:
    x = input("Введите первое число: ")
     
    if is_num(x) == True:
        x = int(x)
    else:
        print("Вы ввели не число")
        continue

    y = input("Введите второе число: ") 

    if is_num(y) == True:
        y = int(y)
    else:
        print("Вы ввели не число")
        continue

    operation = input("Какое действие вы хотите выполнить?(+, -, *, /, **, exit) " )
    match operation:
        case '+':
            print(f"Итог равен: {x + y}")
        case '-':
            print(f"Итог равен: {x - y}")
        case '*':
            print(f"Итог равен: {x * y}")
        case '/':
            if (y == 0) or (x == 0):
                print("На ноль делить нельзя")
            else:
                print(f"Итог равен: {x / y}")
        case '**':
            print(f"Итог равен: {x ** y}")
        case 'exit':
            break
        case _:
            print("Вы ввели неверное действие")
            continue