# 1'. Вычислить число Пи c заданной точностью d
# *Пример:* 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  

from math import pi
d = input("Ввести паттерн числа pi: ")
def needed_example(numer : float, accuracy: float ):
    accuracy = str(accuracy)
    accuracy = len(accuracy[accuracy.find('.')+1::])
    return float (f'{pi:0.{accuracy}f}')
print(needed_example(pi,d))
