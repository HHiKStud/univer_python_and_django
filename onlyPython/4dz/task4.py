fibo_length: int = int(input("Сколько чисел последовательности нужно вывести?: "))
fibonnaci: dict = {1:1,
                   2:1}

def fibo_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        print("Имя: ", func.__name__)
        print("Вызываемые Argsы: ", *args)
        print("Вызываемые Kwargsы: ", *kwargs) #Зачем, их же нет?
        
        return result
    
    return wrapper

@fibo_decorator
def fibonacci_gen(len: int, fibonnaci_dict: dict):
    for i in range(len):
        fibonnaci_dict[i+3] = fibonnaci_dict.get(i+1) + fibonnaci_dict.get(i+2)
        
        yield fibonnaci_dict.get(i+1)

fibo_gen = fibonacci_gen(fibo_length, fibonnaci)

for i in range(fibo_length):
    print(f"{i+1} число: ", next(fibo_gen))