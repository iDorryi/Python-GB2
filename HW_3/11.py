# 1'. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

new_list =[1, 4, 6, 8, 10]
l = len(new_list)
even = []
odd = []
for i in range(l):
    if i%2==0:
        even.append(new_list[i])
    else:
        odd.append(new_list[i])
print("\n Список: {}".format(new_list))
print("\n Количество элементов: {}".format(l))
print("\n Цифры на четных индексах: {},\n Цифры на нечетных индексах: {}\n Сумма цифр на нечетных индексах: {}".format(even, odd, sum(odd)))

# a = [2, 3, 5 , 9, 3]
# print("Сумма цифр на нечетных позициях: {}".format(sum(a[1::2])))