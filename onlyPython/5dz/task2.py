import calendar as cal
import re

date_regex = r"\d{4}-\d{2}" # Задает шаблоном строку в которой идут 4 цифры, тире и 2 цифры. Написал не сам. 
user_date = input("Введите дату в формате ГГГГ-ММ: ")

match = re.match(date_regex, user_date)

if match:
    print(cal.month(int(match.group(0)[:4]), int(match.group(0)[5:])))
else:
    print("Вы неправильно ввели дату.")    


# Часть задания про номер телефона вообще не понял, тут же про дату?

phone_num_regex = r"(?:(?:\+|00)?7|8)[ -]?[\d]{10}" # Это также нашел в интернете. Как я должен сам это написать? :D
phone_num = input("Введите номер телефона(7,8,+7): ")    

match = re.match(phone_num_regex, phone_num)

if match:
    print(match.group(0))
else:
    print("Вы неправильно ввели номер.")    