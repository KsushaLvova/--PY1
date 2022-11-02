main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
new_lower_str = main_str.lower()
letter_dict = {}
for letter in new_lower_str:
    if letter in letter_dict:
        letter_dict[letter] += 1
    else: letter_dict[letter] = 1
print(letter_dict)
