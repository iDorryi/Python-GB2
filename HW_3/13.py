# 3'. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def devision(num:float):
    list1 = str(num).split('.')
    return float('0.'+list1[1])

def max_and_min_difference(list1:list[float]):
    last_list = [devision(i) for i in list1 if int(i) != float(i)]
    print(last_list)
    return max(last_list) - min(last_list)

example = [1.1, 1.2, 3.1, 5, 10.01]
print(max_and_min_difference(example))
