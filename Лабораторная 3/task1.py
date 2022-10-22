src = not False and True or False and not True # исходное задание
my_result = True and True or False and False # избавились от отрицания
my_result_1 = True or False # избавились от логического "И"

result = True  # избавились от логического "ИЛИ"

print(src == result)