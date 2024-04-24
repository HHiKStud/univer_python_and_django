list = []
power = 0

def is_num(elem):
        try:
            float(elem)
            return True
        except ValueError:
            return False

while True:
    amount = input("Сколько чисел вы хотите ввести?: ")
    if is_num(amount) == True:
        if int(amount) > 0:
            for i in range(int(amount)):
                x = input(f"Введите {i+1}-e число: ")
                
                if is_num(x) == True:
                    list.append(int(x))
                else:
                    list.append(x)    

            power = int(input("Введите степень: "))

            for i in range(len(list)):
                if is_num(list[i]) == False:
                    list[i] = list[i] * power
                    print("Элемент " + str(i+1) + ": " + str(list[i]))
                else:    
                    list[i] = list[i] ** power
                    print("Элемент " + str(i+1) + ": " + str(list[i]))
            break             
        else:
            print("Число должно быть положительным.")
            continue
    else:
        print("Вы ввели не число.")
        continue
    