# 2'. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 
init_list = [2, 3, 4, 6]
second_list = [] 
half_list = int(round((len(init_list)+1)/2))
print(half_list)
for i in range(half_list):
    second_list.append(init_list[i]*init_list[len(init_list)-1-i])

print("Первый список: {}".format(init_list))
print("Произведения пар: {}".format(second_list)) 