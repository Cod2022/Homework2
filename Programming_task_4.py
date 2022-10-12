# Задайте список из N элементов, заполненных числами из промежутка [-N, N] (например, [-3, -2, 1, 0, 1, 2, 3]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
n = int(input('Введите число: '))
numbers = list(range(-n, n+1))
write_file = open('file.txt', 'w')
print('Исходный список: ')
for i in numbers:
    string = str(numbers[i-n-1])
    write_file.writelines(f'{string}\n')
    print(string)

print('Результат перемножения элементов:')
result = 1
with open('file.txt', 'r') as read_file:
    for g in range(0, n*2):
        pos = int(g)
        result *= numbers[pos]
        text = read_file.readlines()
print(result)
    
    
    
# string = str(numbers)
# print(numbers)
# for i in numbers:
    # print(string[23])
# print(positions)