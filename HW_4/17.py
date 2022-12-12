# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]
n = int(input("Введите число: "))
def mult_list(n = int, uniq: bool = False):
    mult = []
    i = 2
    while n != 1:
        while n % i == 0:
            mult.append(i)
            n //= i
        i += 1
    if uniq: 
        return list(set(mult))
    else:
        return mult
    
print("Простые множители числа: {}".format(mult_list(n)))
print("Неповторяющиеся простые множетели числа: {}".format(mult_list(n, True)))

