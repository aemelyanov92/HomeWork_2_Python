# 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами
# из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

pos_1 = int(input("Введите первую позицию: "))
pos_2 = int(input("Введите вторую позицию: "))
num = int(input("введите число: "))
ls = []
for i in range(-num, num + 1):
    ls.append(i)
A = list(range(num*(-1), num+1))
print(ls)
print(A[pos_1-1]*A[pos_2-1])

