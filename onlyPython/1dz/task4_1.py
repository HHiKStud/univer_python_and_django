ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З3К2"

while True:
    x = input("Какую клетку вы хотите атаковать?: ")

    if x.upper() in ship:
        print("Вы попали!")
        ship.replace(ship[x], '')
        continue
    else:
        print("Вы промахнулись!")
        continue
