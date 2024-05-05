from contextlib import contextmanager

@contextmanager
def my_cntx_man(file_name: str):
    file = open(file_name, mode="a+", encoding="utf-8")
    
    try:
        yield file
    
    except Exception:
        raise        
    
    finally:
        file.close()

def open_file(file_name: str, text: str):
    with my_cntx_man(file_name) as cntx_man:
        cntx_man.write(f"\n{text}")

user_text = input("Что хотите дозаписать?: ")

open_file("test.txt", user_text)

#Сделал так, потому что при mode="a+" читать строки не получается, возвращается пустой список
with open("test.txt") as file:
    text = file.readlines()

    for l in text:
        if (text.index(l)+1) % 2 == 0:
            print(l)

    file.close()