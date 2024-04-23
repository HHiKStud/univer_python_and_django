while True:
    x = int(input("Введите 3-х значное число без повторяющихся цифр: "))
    if len(str(x)) != 3:
        print("Число должно быть трёхзначным!")
        continue
    else:
        for i in str(x):
            if str(x).count(i) > 1:
                print("Число должно быть без повторов!")
                break
            else:
                a = x % 10 
                b = (x % 100) // 10 
                c = x // 100

                print(a,b,c,sep='') 
                print(a,c,b,sep='') 
                print(b,a,c,sep='') 
                print(b,c,a,sep='') 
                print(c,a,b,sep='') 
                print(c,b,a,sep='')
                break
        break