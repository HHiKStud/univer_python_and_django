natural_nums: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def nat_list_comp(nums: list) -> list:
    return [num**2 for num in nums]

print("1: ", nat_list_comp(natural_nums))

#--------------------------------
week_days:list = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

def week_days_dict_comp(weekdays: list) -> dict:
    return {day: weekdays.index(day)+1 for day in weekdays}

print("2: ", week_days_dict_comp(week_days))

#---------------------------------
libraries: list = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
def libraries_set_comp(libs: list) -> set:
    return {lib.lower() for lib in libs}

print("3: ", libraries_set_comp(libraries))
# Как можно заметить, при генерации сета все повторяющиеся элементы были заменены одним