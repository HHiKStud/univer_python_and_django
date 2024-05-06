def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num)/len(list_num), 2)

assert average_num([1, 2, 3]) == 2.0
assert average_num([1, 2, 3]) == 2
assert average_num([1, -2, -5]) == -2.0
assert average_num([1, -2, -5]) == -2
assert average_num([1.0, 2.0, 3.0]) == 2
assert average_num([1, "a", 3]) == "Bad request"
assert average_num(["1", "2", "3"]) == 2
assert average_num([1, "2", "3"]) == 2
assert average_num([["1"], ["2"], ["3"]]) == "Bad request"
