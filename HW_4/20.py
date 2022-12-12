# 5'. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9
import sympy
from sympy import simplify
import random
# from random import randint as rnd
def get_polinom(k: int, simple: bool = True) -> str:
    polinom = ''
    for i in range(k, -1, -1):
        polinom += f'{random.randrange(0,100)}*x**{i}+'
        if i == 0:
            polinom += f'{random.randrange(0,100)}*x**{i}'
    if simple:
        return str(sympy.simplify(polinom))
    else:
        return str(polinom)


k = int(input("Введите степень: "))

pol1 = get_polinom(k)
print(f'Сгенерированный полином 1 {pol1}')
pol2 = get_polinom(k)
print(f'Сгенерированный полином 2 {pol2}')


# f1 = open('file1.txt','w')
with open('file1.txt','w') as f1:
        f1.write(pol1)

# f2 = open('file2.txt','w')
with open('file2.txt','w') as f2:
        f2.write(pol2)

sum_of_polinoms = simplify(pol1 + '+' + pol2)
sum_of_polinoms = str(sum_of_polinoms)
print(f'Сумма полиномов 1 и 2: {sum_of_polinoms}')

# f3 = open('file3.txt','w')
with open('file3.txt','w') as f3:
        f3.write(sum_of_polinoms)



