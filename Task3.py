# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
n = int(input('Введите число: '))
ls = list()
for k in range(1, n+1):
    func = round(((1 + 1 / n) ** n))
    ls.append(func)
print(ls)
print(sum(ls))