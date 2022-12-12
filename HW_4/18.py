# 3'. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


numbers = list(map(int,input().split()))

def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)
    for number in unique_numbers:
        list_of_unique_numbers.append(number)
    return list_of_unique_numbers

print("Начальный список с повторяющимеся значениями {}".format(numbers))
print("Список уникальных значений {}".format(get_unique_numbers(numbers)))
