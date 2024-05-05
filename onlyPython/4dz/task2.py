fibo_length: int = int(input("Сколько чисел последовательности нужно вывести?: "))
fibonnaci: dict = {1:1,
                   2:1}

def fibonacci_gen(len: int, fibonnaci_dict: dict):
    for i in range(len):
        fibonnaci_dict[i+3] = fibonnaci_dict.get(i+1) + fibonnaci_dict.get(i+2)
        
        yield fibonnaci_dict.get(i+1)

fibo_gen = fibonacci_gen(fibo_length, fibonnaci)

for i in range(fibo_length):
    print(f"{i+1} число: ", next(fibo_gen))