vars: list = []
vars_result1: list = []
vars_result2: list = []

def multipl(*vars, mult=2):
    for var in vars:
        vars_result1.append(var * mult)
        print(f"{var}: {vars_result1[var-1]}")

amount = int(input("Сколько значений вы хотите ввести?: "))

for i in range(amount):
    x = int(input(f"Введите {i+1}-е число: "))
    vars.append(x)

multiplier = int(input("На какое число умножить?: "))

multipl(*vars, mult = multiplier)

#-------------------------------

multipl2 = lambda *vars, mult=multiplier:   [vars_result2.append(var * mult) for var in vars]
multipl2(*vars, mult = multiplier)
print(vars_result2)