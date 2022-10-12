# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
n = int(input('Введите число: '))
list = list(range(1, n+1))
result = 1
print(f'Набор произведений чисел от 1 до {n}: ')
for i in list:
    result = result * list[i-1]
    print(result)
