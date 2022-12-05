# 5'. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]



# fib1 = fib2 = 1
# n = int(input ("Номер элемента ряда Фибоначчи: "))
# i = 0
# while i < n-2: 
#     sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = sum

def fibonacci(n):
    if n == 0:
        return(0)
    elif n in (1, 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print("Значение элемента Фибоначчи {}".format(fibonacci(n = int(input("Введите номер элемента Фибоначчи: ")))))
k = int(input("Введите количество элементов Фибоначчи: "))
list1 =[]
for i in range (0,k+1):
    list1.append(fibonacci(i))
print("Положительный список чисел Фибоначи: {}".format(list1))

list2 = [((-1)**(i+1))*fibonacci(i) for i in range(1,k+1)]
list2.reverse()
print("Отрицательный список чисел Фибоначи: {}".format(list2))
print("Общий список: {}".format(list2+list1))


   














