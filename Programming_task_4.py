# Задайте список из N элементов, заполненных числами из промежутка [-N, N] (например, [-3, -2, 1, 0, 1, 2, 3]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
n = int(input('Введите число: '))
numbers = list(range(-n, n+1))
# for i in range(-n, n+1):
    # print(i)
string = str(numbers)
print(numbers)
with open('file.txt', 'w') as positions:
    positions.writelines(string)
print(positions)