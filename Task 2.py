# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите целое число: '))
print(type(number))
factor = 1
list = []
for i in range(1, number + 1):
    factor = factor * i
    list.append(factor) 
print(f"Произведения чисел от 1 до {number}:  {list}")